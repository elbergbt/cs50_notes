# my version
# def main():
#     x = int(input("what is x? "))
#     odd_or_even(x)
#
# def odd_or_even(number: int):
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
# main()

#lecture's version

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

main()

# simpler 1

def is_even(number):
    return True if number % 2 == 0 else False

# simpler 2

def is_even(number):
    return number % 2 == 0