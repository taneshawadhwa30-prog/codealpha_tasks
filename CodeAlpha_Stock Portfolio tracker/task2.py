stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}

stock_name = input("Enter stock name (AAPL, TSLA, GOOGL, MSFT): ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:
    total = stock_prices[stock_name] * quantity
    print("Total Investment Value: $", total)

    file = open("portfolio.txt", "w")
    file.write("Total Investment Value: $" + str(total))
    file.close()

    print("Result saved in portfolio.txt")
else:
    print("Stock not found")