# store name in variable

name = input("What is your name? ")
print("Hello,", name)

# store names in a list

names = []

for _ in range(3):
    names.append(input("What is your name? "))

for name in sorted(names):
    print(f"Hello, {name}")

# write to a file

name = input("What is your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()

# appends to a file

name = input("What is your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# adds context manager

name = input("What is your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# reads from a file

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())  # .rstrip removes spaces, tabs, and newline characters

# reads from a file, one line at a time

with open("names.txt", "r") as file:
    for line in file:
        print("hello, ", line.rstrip())

