def main():
    x = gey_int()
    print(f"x is {x}")



def gey_int():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            pass # no message cycle continue


main()