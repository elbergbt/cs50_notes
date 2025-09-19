import sys

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        if len(names) == 1:
            sys.exit(f"Adieu, adieu, to {names[0]}")
        else:
            a = ", ".join(names[:-1])
            sys.exit(f"Adieu, adieu, to {a} and {names[-1]}") # names[-1] - last name

