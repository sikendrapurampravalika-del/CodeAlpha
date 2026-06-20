# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300,
    "AMZN": 200
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Result saved in portfolio.txt")
