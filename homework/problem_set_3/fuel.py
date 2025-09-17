def main():
    fraction = get_fraction()
    print(fraction)


def get_fraction():
    while True:
        try:
            fraction = input("what is fraction? ")
            x,y = fraction.split("/")
            percentage = int(x) / int(y) * 100

        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            break

    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{round(percentage)}%"


main()