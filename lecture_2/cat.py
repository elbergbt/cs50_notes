#while

# version 1
i = 3
while i != 0:
    print("meow")
    i -= 1

# version 2

i = 0
while i < 3:
    print("meow")
    i +=1

# for

for i in range(3):   # for _ in range(3) //// i == _ if this variable is useless in this code
    print("meow")

# just print

print("meow\n" * 3, end = "")