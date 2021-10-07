rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter number of symbol: ")

for i in range(0, rows+1):
    for j in range(0, columns+1):
        print(symbol, end="")
    print()

