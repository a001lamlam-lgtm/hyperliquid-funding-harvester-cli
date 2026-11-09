# Hyperliquid Funding Rate Harvester & Solana Alpha Radar ⚡

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hyperliquid](https://img.shields.io/badge/Hyperliquid-L1-black)](https://hyperliquid.xyz)
[![Solana](https://img.shields.io/badge/Solana-DeFi-purple)](https://solana.com)

An autonomous, zero-dependency Python quant engine designed to monitor 230+ perpetual contracts on Hyperliquid L1 for extreme funding rate dislocations (APR > 50% / < -50%) and track real-time liquidity/volume breakouts across Solana and Base DEXs.

---

## 🚀 Key Features

- **⚡ Zero Paid API Keys**: Uses public read endpoints from Hyperliquid L1 and DEX Screener. Zero monthly SaaS fees.
- **📈 Real-Time Funding APR Calculation**: Converts raw hourly funding rates into annualized APR across 230+ assets.
- **🛡️ Delta-Neutral Strategy Generator**: Identifies when to Short Perp or Long Perp to capture high yield without directional market risk.
- **🛰️ Solana & Base Momentum Radar**: Flags 1h/24h volume surges, price breakouts, and high-liquidity pools.
- **💻 Ultra-Lightweight**: Built 100% on standard Python libraries. Runs anywhere from a laptop to a $5 cloud VPS.

---

## 📊 Live Market Scans & Alpha Feed

Check our automated 6-hour on-chain feed:
👉 **[View Latest Market Alpha & Arbitrage Dispersions (Updated 24/7)](LATEST_MARKET_ALPHA.md)**

| Asset | Annualized APR | Hourly Rate | Directional Strategy |
| :--- | :--- | :--- | :--- |
| **XMR** | **+103.3%** | +0.0118% / hr | 🟢 Short Perp (Collect Hourly Funding) |
| **INIT** | **-1842.1%** | -0.2103% / hr | 🔵 Long Perp (Collect Hourly Funding) |
| **MEME** | **-131.1%** | -0.0150% / hr | 🔵 Long Perp (Collect Hourly Funding) |

---

## 🛠️ Quickstart

### 1. Clone & Run Hyperliquid Harvester
```bash
git clone https://github.com/a001lamlam-lgtm/hyperliquid-funding-harvester-cli.git
cd hyperliquid-funding-harvester-cli
python3 hyperliquid_harvester.py
```

### 2. Run Solana & Base Alpha Radar
```bash
python3 solana_base_radar.py
```

---

## 💰 Support the Project / Web3 Pro License

If this tool helps you find alpha or capture funding yields, consider sponsoring or unlocking custom private strategies:

* **EVM (Base / Arbitrum / Polygon / Ethereum)**:
  `0xb583a09D4358Dd8A992F219328342BabeEb5751C` (USDC / ETH)
* **Solana**:
  `5nDKyxqUvRUrSLzhviHDBQb9hoh7ZbzhL6ASDdFKdCXv` (SOL / USDC)

---

## 📜 License
MIT License. Free for open-source and individual usage.
