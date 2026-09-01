# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}

print("Welcome to Stock Portfolio Tracker")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", price)

stock_name = input("\nEnter stock name: ").upper()

if stock_name in stock_prices:
    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]
    total_investment = price * quantity

    print("\nStock Name:", stock_name)
    print("Price per Share:", price)
    print("Quantity:", quantity)
    print("Total Investment:", total_investment)

else:
    print("Stock not found!")
