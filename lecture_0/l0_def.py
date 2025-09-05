# def = define (your own function)

def hello(to = "world"):
    print("Hello,", to)

hello()

name = input("What is your name? ")

hello(name)

####################################

def main():
    name = input("what is your name? ")
    hello()

def hello(to = "world"):
    print("hello", to)

main()