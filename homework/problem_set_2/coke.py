amount = 50

while amount > 0:
    print(f"Amount Due: {amount}")
    coin = int(input("Insert coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        amount = amount - coin

    if amount < 0:
        print(f"Change Owed: {abs(amount)}", end ="")