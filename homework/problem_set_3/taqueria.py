total = 0
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

while True:
    try:
        order = input("Item: ").title() # case-insensitive matching
        total += menu[order]
        print(f"Total: ${total:.2f}") # formatted to 2 decimals

    except EOFError: # PyCharm read Ctrl-D as kill console or detach session, not send EOF
        print()
        break
    except KeyboardInterrupt: # KeyboardInterrupt instead of EOFError
        print("\nExiting...")
        break
    except KeyError:
        pass