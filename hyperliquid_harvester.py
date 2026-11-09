#!/usr/bin/env python3
"""
Heo đi bộ - Hyperliquid Real-Time Funding Rate Arbitrage Engine
Scans 230+ perpetual contracts on Hyperliquid L1, identifies extreme funding spreads
(e.g., APR > 50% or APR < -50%), and generates delta-neutral yield strategies.
100% on-chain DeFi arbitrage.
"""

import urllib.request
import json
from datetime import datetime

HYPERLIQUID_API = "https://api.hyperliquid.xyz/info"

def fetch_hyperliquid_market_data():
    payload = {"type": "metaAndAssetCtxs"}
    req = urllib.request.Request(
        HYPERLIQUID_API,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json", "User-Agent": "HeoDiBo-Quant/1.0"}
    )
    with urllib.request.urlopen(req, timeout=12) as resp:
        data = json.loads(resp.read().decode())
        meta = data[0]["universe"]
        ctxs = data[1]
        
        results = []
        for asset, ctx in zip(meta, ctxs):
            name = asset["name"]
            funding_raw = float(ctx.get("funding", 0))
            # Hyperliquid funding is hourly. Annualized APR = hourly * 24 * 365 * 100
            apr = funding_raw * 24 * 365 * 100
            px = float(ctx.get("oraclePx", 0))
            vol_24h = float(ctx.get("dayNtlVlm", 0))
            open_interest = float(ctx.get("openInterest", 0)) * px

            results.append({
                "asset": name,
                "apr": apr,
                "hourly_rate": funding_raw * 100,
                "price": px,
                "volume_24h": vol_24h,
                "open_interest": open_interest
            })
        return results

def get_top_yield_opportunities(min_volume=200000):
    markets = fetch_hyperliquid_market_data()
    # Filter for liquid markets
    filtered = [m for m in markets if m["volume_24h"] >= min_volume]
    
    # Sort by absolute APR
    filtered.sort(key=lambda x: abs(x["apr"]), reverse=True)
    return filtered

def generate_arbitrage_report():
    opps = get_top_yield_opportunities()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = f"# HYPERLIQUID REAL-TIME FUNDING YIELD REPORT ⚡\n"
    report += f"*Cập nhật tự động lúc {timestamp} - Heo đi bộ Quant Engine*\n\n"
    report += "| Tài sản | APR Hàng Năm | Lãi Giờ (Hourly) | Giá Oracle | Volume 24h | Chiến lược Thu Tiền |\n"
    report += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
    
    for opp in opps[:10]:
        strategy = "🟢 SHORT PERP (Nhận lãi)" if opp['apr'] > 0 else "🔵 LONG PERP (Nhận lãi)"
        report += f"| **{opp['asset']}** | **{opp['apr']:+.1f}%** | {opp['hourly_rate']:+.4f}% | ${opp['price']:,.2f} | ${opp['volume_24h']:,.0f} | {strategy} |\n"
        
    return report, opps

if __name__ == "__main__":
    report_text, top_opps = generate_arbitrage_report()
    print(report_text)
