def stock_portfolio_tracker():
    stock_prices = {
        "AAPL": 180.00,
        "MSFT": 420.50,
        "GOOGL": 175.25,
        "AMZN": 185.70,
        "TSLA": 250.00,
        "NVDA": 1000.00,
        "META": 490.10
    }
    portfolio = {}
    total_value = 0.0
    print("📊 --- Stock Portfolio Tracker --- 📊\n")
    print("Available Stocks:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price:.2f}")

    print("\nEnter your stock holdings. Type 'done' when finished.\n")
    while True:
        stock = input("Enter stock symbol (e.g., AAPL) or 'done': ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("❌ Invalid stock symbol. Please try again from the list.")
            continue
        while True:
            try:
                qty = int(input(f"Enter quantity for {stock}: "))
                if qty <= 0:
                    print("⚠️ Quantity must be positive.")
                    continue
                break
            except ValueError:
                print("⚠️ Please enter a valid integer.")
        portfolio[stock] = portfolio.get(stock, 0) + qty
        print(f"✅ Added {qty} share(s) of {stock}.\n")
    print("\n📃 --- Portfolio Summary ---")
    if not portfolio:
        print("⚠️ Your portfolio is empty.")
        return
    summary_lines = []
    summary_lines.append("📃 --- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        investment = price * qty
        total_value += investment
        line = f"{stock}: {qty} share(s) × ${price:.2f} = ${investment:.2f}"
        print(line)
        summary_lines.append(line)
    total_line = f"\n💰 Total Investment Value: ${total_value:.2f}"
    print(total_line)
    summary_lines.append(total_line)
    save = input("\nDo you want to save this summary to a file? (yes/no): ").strip().lower()
    if save == 'yes':
        try:
            with open("stock_portfolio_summary.txt", "w") as file:
                file.write("\n".join(summary_lines))
            print("📂 Summary saved to 'stock_portfolio_summary.txt'")
        except Exception as e:
            print(f"❌ Failed to save file: {e}")
    else:
        print("📁 Summary not saved.")
if __name__ == "__main__":
    stock_portfolio_tracker()
