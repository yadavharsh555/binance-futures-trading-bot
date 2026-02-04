📈 Binance Futures Testnet Trading Bot (Python)

A CLI-based Python application that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).
The project is structured, reusable, and includes proper validation, logging, and error handling.

🎯 Objective

Build a simplified trading bot that:

Connects to Binance Futures Testnet

Places BUY/SELL orders

Supports MARKET and LIMIT orders

Uses a clean architecture with logging and error handling

🚀 Features

Python 3.x

Binance Futures USDT-M Testnet

Order Types:

MARKET

LIMIT

Order Sides:

BUY

SELL

Command Line Interface (CLI)

Input validation

Structured, modular code

File-based logging

Graceful exception handling

📁 Project Structure
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance Futures client wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging configuration
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
└── logs/
    └── trading_bot.log

🛠 Prerequisites

Python 3.8+

Binance Futures Testnet account

Testnet API Key & Secret

Internet connection

🔧 Setup Instructions
1️⃣ Clone the Repository
git clone <your-github-repo-url>
cd trading_bot

2️⃣ (Optional) Create Virtual Environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file in the project root:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret


⚠️ Use only Binance Futures Testnet keys
⚠️ Do NOT commit .env to GitHub

5️⃣ Get Testnet USDT Balance

Visit https://testnet.binancefuture.com

Login using Google / GitHub

Go to Wallet

Click Get Testnet Funds

Ensure USDT balance is available

▶️ How to Run the Application

Make sure you are in the project root:

PS E:\trading_bot>

✅ Place a MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

✅ Place a LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000

📤 Sample Output
--- ORDER SUMMARY ---
Order ID     : 12345678
Status       : NEW
Executed Qty : 0.001
Avg Price    : N/A
Order placed successfully ✅

📝 Logging

All API requests, responses, and errors are logged to:

logs/trading_bot.log


The log file includes:

One MARKET order

One LIMIT order

Any API or network errors

(This file is attached during submission as required.)

⚠️ Error Handling

The application handles:

Invalid CLI inputs

Missing required parameters

API errors

Network or testnet failures

Errors are logged and displayed cleanly.

🧠 Assumptions

User has sufficient testnet USDT balance

Orders are placed on USDT-M Futures

Default leverage is used

Uses the official Binance Futures SDK (binance-futures-connector) for better testnet stability

🧪 Tested Environment

Python 3.12

Windows (PowerShell)

Binance Futures Testnet

binance-futures-connector SDK

📦 Dependencies
binance-futures-connector
python-dotenv