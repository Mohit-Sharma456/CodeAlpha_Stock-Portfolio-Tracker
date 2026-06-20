# Stock Portfolio Tracker

# Hardcoded stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140
}

total = 0

while True:
    stock_name = input("Enter stock name (or 'done' to stop): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))

        value = stocks[stock_name] * quantity
        total = total + value

        print("Investment Value =", value)

    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total)

# Save result in text file
file = open("portfolio.txt", "w")
file.write("Total Investment Value = " + str(total))
file.close()

print("Result saved in portfolio.txt")