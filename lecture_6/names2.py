# appends names to a list for sorting

names = []

with open("names.txt") as file:   # "r" as default, but not "w", "a" etc.
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print("hello,", name)

# version 2

with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())