# compare/ if/elif/else

x = int(input("whats is x? "))
y = int(input("what is y? "))

if x < y :
    print("x is less than y")
elif x > y :
    print("x is greater than y")
else:
    print("they are equal")

# or

x = int(input("whats is x? "))
y = int(input("what is y? "))

if x < y or x > y :   # we get true if one of them is right, in case where both expression if false we get false
    print("they are mot equal")
else:
    print("they are equal")

#simpler version

x = int(input("whats is x? "))
y = int(input("what is y? "))

if x != y :   # we get true if one of them is right, in case where both expression if false we get false
    print("they are mot equal")
else:
    print("they are equal")


