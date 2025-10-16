import sys
import os
import csv

from tabulate import tabulate


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]

        if not is_exist(filename):
            sys.exit("File does not exist")
        if not is_csv(filename):
            sys.exit("Not a CSV file")

        with open("sicilian.csv", "r") as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, headers = "keys", tablefmt="grid"))

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


def is_exist(filename):
    return os.path.isfile(filename)

def is_csv(filename):
    return filename.endswith(".csv")



if __name__ == "__main__":
    main()