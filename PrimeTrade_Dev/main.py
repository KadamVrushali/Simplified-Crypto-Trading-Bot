import os
from dotenv import load_dotenv
from basic_bot import BasicBot
from tabulate import tabulate

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_SECRET_KEY")

if not api_key or not api_secret:
    print("Error: API keys not found. Please set BINANCE_API_KEY and BINANCE_SECRET_KEY in your .env file.")
    exit()

def display_account_info(bot):
    balances = bot.get_account_balance()
    print("\n=== ACCOUNT BALANCE ===")
    print(tabulate(balances, headers="keys", tablefmt="fancy_grid"))

def get_user_input():
    symbol = input("Enter trading symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Enter order type (MARKET/LIMIT/STOP_MARKET): ").upper()

    try:
        quantity = float(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return None, None, None, None, None, None

    price = None
    stop_price = None

    if order_type == 'LIMIT':
        try:
            price = float(input("Enter price for LIMIT order: "))
        except ValueError:
            print("Invalid price. Please enter a number.")
            return None, None, None, None, None, None

    if order_type == 'STOP_MARKET':
        try:
            stop_price = float(input("Enter stop price for STOP_MARKET order: "))
        except ValueError:
            print("Invalid stop price. Please enter a number.")
            return None, None, None, None, None, None

    if side not in ['BUY', 'SELL'] or order_type not in ['MARKET', 'LIMIT', 'STOP_MARKET']:
        print("Invalid side or order type.")
        return None, None, None, None, None, None

    return symbol, side, order_type, quantity, price, stop_price


if __name__ == "__main__":
    bot = BasicBot(api_key=api_key, api_secret=api_secret)

    print("=== Welcome to the Simplified Trading Bot CLI ===")

    while True:
        print("\nSelect an option:")
        print("1. View Account Balance")
        print("2. Place a New Order (Market / Limit / Stop-Limit)")
        print("3. Check Open Orders")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_account_info(bot)

        elif choice == '2':
            display_account_info(bot)  # Show balance before trading
            # Show available symbols before asking for symbol input
            print("\nFetching available symbols...")
            symbols = bot.get_available_symbols()
            if symbols:
                print("Available symbols:")
                print(", ".join(symbols))

            symbol, side, order_type, quantity, price, stop_price = get_user_input()
            if symbol:
                print(f"\nYou are about to place an order:")
                print(f"Symbol: {symbol}, Side: {side}, Type: {order_type}, Quantity: {quantity}, Price: {price}, Stop Price: {stop_price}")
                confirm = input("Confirm order? (y/n): ").lower()
                if confirm == 'y':
                    bot.place_order(symbol, side, order_type, quantity, price, stop_price)
                else:
                    print("Order cancelled.")

        elif choice == '3':
            print("\nFetching available symbols...")
            symbols = bot.get_available_symbols()
            if symbols:
                print("Available symbols:")
                print(", ".join(symbols))
            symbol = input("Enter symbol to check open orders for (e.g., BTCUSDT): ").upper()
            if symbol:
                bot.get_open_orders(symbol)

        elif choice == '4':
            print("Exiting bot. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
