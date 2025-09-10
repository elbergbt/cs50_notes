# check if user input is positive number

while True:
    i = int(input("What is i? "))
    if i < 0:
        continue
    else:
        break

# how to make it shorter?

while True:
    i = int(input("What is i ?"))
    if i > 0:
        break

for _ in range(i):
    print("meow")