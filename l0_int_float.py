#int

x = int(input("what is x? "))
y = int(input("what is y? "))

# z = int(x) + int(y)

print(x + y)

#float

x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x + y)

print(z)

z = round(x / y, 2) # 2/3 = 0,666666... with round 2 it will be 0,67
print(f'{z:.2f}') # is the same that upper line