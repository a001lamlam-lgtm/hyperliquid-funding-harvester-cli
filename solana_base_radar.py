#!/usr/bin/env python3
"""
Heo đi bộ - Solana & Base Real-Time DEX Alpha Radar
Tracks explosive volume breakouts, new high-liquidity pairs, and momentum runners
across Solana and Base DEXs without requiring paid API keys.
"""

import urllib.request
import json
from datetime import datetime

DEX_SEARCH_URL = "https://api.dexscreener.com/latest/dex/search?q="

def scan_chain_momentum(query="USDC", target_chains=["solana", "base"]):
    url = DEX_SEARCH_URL + query
    req = urllib.request.Request(url, headers={"User-Agent": "HeoDiBo-Radar/1.0"})
    
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode())
            pairs = data.get("pairs", [])
            
            filtered = []
            for p in pairs:
                chain = p.get("chainId")
                if chain in target_chains:
                    vol_1h = float(p.get("volume", {}).get("h1", 0) or 0)
                    vol_24h = float(p.get("volume", {}).get("h24", 0) or 0)
                    price_change_1h = float(p.get("priceChange", {}).get("h1", 0) or 0)
                    liquidity = float(p.get("liquidity", {}).get("usd", 0) or 0)
                    
                    # Filter for active, liquid pools (avoid illiquid scams)
                    if liquidity > 25000 and vol_24h > 50000:
                        filtered.append({
                            "chain": chain.upper(),
                            "pair": f"{p.get('baseToken', {}).get('symbol')}/{p.get('quoteToken', {}).get('symbol')}",
                            "price_usd": float(p.get("priceUsd", 0) or 0),
                            "change_1h": price_change_1h,
                            "vol_1h": vol_1h,
                            "vol_24h": vol_24h,
                            "liquidity": liquidity,
                            "dex": p.get("dexId"),
                            "url": p.get("url")
                        })
            
            # Sort by 1h volume momentum
            filtered.sort(key=lambda x: x["vol_1h"], reverse=True)
            return filtered
    except Exception as e:
        print(f"[!] Error querying DEX Screener: {e}")
        return []

def generate_radar_report():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sol_opps = scan_chain_momentum("SOL", target_chains=["solana"])
    base_opps = scan_chain_momentum("ETH", target_chains=["base"])
    
    all_opps = sol_opps[:5] + base_opps[:5]
    
    report = f"# SOLANA & BASE REAL-TIME ALPHA RADAR 🛰️\n"
    report += f"*Cập nhật tự động lúc {timestamp} - Heo đi bộ Radar*\n\n"
    report += "| Mạng | Cặp Giao Dịch | Giá USD | Biến động 1h | Vol 1h | Vol 24h | Thanh khoản |\n"
    report += "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"
    
    for o in all_opps:
        change_str = f"🟢 +{o['change_1h']}%" if o['change_1h'] > 0 else f"🔴 {o['change_1h']}%"
        report += f"| **{o['chain']}** | [{o['pair']}]({o['url']}) | ${o['price_usd']:,.4f} | {change_str} | ${o['vol_1h']:,.0f} | ${o['vol_24h']:,.0f} | ${o['liquidity']:,.0f} |\n"
        
    return report, all_opps

if __name__ == "__main__":
    rep, items = generate_radar_report()
    print(rep)
