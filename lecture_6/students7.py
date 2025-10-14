# writes a .csv file using csv.writer

import csv

name = input("What is your name? ")
home = input("Where is your home? ")

with open("students_homes2.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
