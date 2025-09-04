#variables and functions

name = input("what is your name? ")

# remove whitespace from str
name = name.strip()

# capitalize user's name, but capitalize only first letter
name = name.capitalize()

#capitalize first letter of each word
name = name.title()

#remove whitespace from str and capitalize user's name
name = name.strip().title()

# the short way
#name = input("What is your name?").strip().title()

#split the user's name into first name and last name
first, last = name.split(" ")

print('Hello, ', end="")
print(name)

#other options to print
print('Hello ' + name)
print('Hello', name)
print(f'Hello, {name}') # format string