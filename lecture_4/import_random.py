import random

# from random import choice
# coin = choice(["heads", "tails"])

# choice
coin = random.choice(["heads", "tails"])
print(coin)

# randint
number = random.randint(1, 10) # random number from 1 to 10
print(number)

# shuffle
cards = ["queen", "king", "jack"]
random.shuffle(cards)

for card in cards:
    print(card)