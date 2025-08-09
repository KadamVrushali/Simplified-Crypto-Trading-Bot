

# 🚀 Simplified Crypto Trading Bot

A **Python-based command-line interface (CLI)** for placing **Market**, **Limit**, and **Stop-Market** orders on the **Binance Futures Testnet**.  
Trade in a **risk-free environment** while learning how to interact with the Binance API for futures trading.

---

## ✨ Features

- **🔗 Binance Futures Testnet Integration** – Uses the official [`python-binance`](https://github.com/sammchardy/python-binance) library for safe simulated trading.
- **📈 Multiple Order Types** – Supports `MARKET`, `LIMIT`, and `STOP_MARKET` orders.
- **💻 Interactive CLI** – Simple yet functional menu-based trading interface.
- **💰 Account Management** – View your testnet balance and asset holdings.
- **📜 Order Tracking** – Check the status of open orders for any symbol.

---

## 🛠 Getting Started

Follow these steps to set up and run the bot locally.

### **1️⃣ Prerequisites**
- Python **3.7+**
- A Binance **Futures Testnet** account & API keys → [Get them here](https://testnet.binancefuture.com/)

---

### **2️⃣ Installation**

```bash
# Clone the repository
git clone https://github.com/KadamVrushali/Simplified-Crypto-Trading-Bot.git
cd Simplified-Crypto-Trading-Bot

# Install dependencies
pip install -r requirements.txt
````

---

### **3️⃣ Configuration**

1. Create a `.env` file in the project root.
2. Add your Binance Testnet API credentials:

```
BINANCE_API_KEY=YOUR_TESTNET_API_KEY
BINANCE_SECRET_KEY=YOUR_TESTNET_SECRET_KEY
```

⚠ **Keep your `.env` private** 

---

## ▶ Usage

Run the bot:

```bash
python main.py
```

### 📋 CLI Menu Options:

1. **View Account Balance** – Shows available assets and balances.
2. **Place a New Order** – Create a `MARKET`, `LIMIT`, or `STOP_MARKET` order.
3. **Check Open Orders** – View all active orders for a chosen symbol.
4. **Exit** – Close the application.

---

## 📂 Project Structure

```
├── main.py          # CLI entry point
├── basic_bot.py     # Core Binance API logic
├── requirements.txt # Python dependencies
├── .env             # API credentials (not committed to Git)
```

---

## 🎯 Bonus Features Implemented

✅ **Advanced Order Type** – Added `STOP_MARKET` support.
✅ **Enhanced CLI** – Account balance shown before trades, improved prompts, and available symbols listing.

---

## 🤝 Contributing

Pull requests are welcome!
Fork the repo and submit improvements, bug fixes, or new features.

---

## 📜 License

This project is licensed under the **MIT License** – see [`LICENSE`](LICENSE) for details.

