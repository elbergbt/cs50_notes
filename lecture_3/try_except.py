# version 1
# try:
#     x = int(input("What is x? "))
#     print(f"x is {x}")
#
# except ValueError:
#     print("x is not an integer")

# version 2
# try:
#     x = int(input("What is x? "))
#
# except ValueError:
#     print("x is an integer!")
# else:
#     print(f"x is {x}")

# version 3

while True:
    try:
        x = int(input("what is x? "))
    except ValueError:
        print("x is an integer!")
    else: break

print(f"x is {x}")
