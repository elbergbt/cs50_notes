#calculator with functions

def main():
    x = int(input("what is x? "))
    print("x squared is", square(x))

def square(n):
    return n * n # n ** 2 /// pow(n, 2 )

main()