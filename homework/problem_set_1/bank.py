greet = input("Greeting: ").lower()

if greet.find("hello") != -1:
    print("$0")
elif greet.find("h", 0,1) != -1:
    print("$20")
else:
    print("$100")

