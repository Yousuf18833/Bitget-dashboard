
import streamlit as st
import requests
import feedparser
import datetime

st.set_page_config(page_title="Bitcoin Region Tracker", layout="wide")
st.title("📊 Bitcoin Tracker Dashboard")

# --- Whale Alert (mock data for demo) ---
st.header("🐋 Whale Alert - Recent Large BTC Transactions")

# Mock data (replace with actual API integration if available)
transactions = [
    {"from": "Unknown Wallet", "to": "Binance", "amount": 1234, "currency": "BTC"},
    {"from": "Bitfinex", "to": "Unknown Wallet", "amount": 987, "currency": "BTC"},
    {"from": "Coinbase", "to": "Kraken", "amount": 650, "currency": "BTC"},
]

for tx in transactions:
    st.write(f"💸 {tx['amount']} {tx['currency']} transferred from {tx['from']} to {tx['to']}")

# --- Bitcoin News using RSS Feed ---
st.header("🗞️ Latest Bitcoin News")

feed = feedparser.parse("https://news.bitcoin.com/feed/")
for entry in feed.entries[:5]:
    st.markdown(f"**[{entry.title}]({entry.link})**")
    st.caption(entry.published)

# --- Placeholder for your region-wise tracking code ---
st.header("📍 Region-wise Bitcoin Buying/Selling (Coming Soon)")
st.info("This section will display live regional Bitcoin buying/selling stats when integrated.")
