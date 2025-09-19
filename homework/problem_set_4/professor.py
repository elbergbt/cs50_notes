import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        result = a + b
        for attempt in range(3):
            try:
                x =  int(input(f"{a} + {b} = "))
                if x == result:
                    score +=1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
        else:
            # executed only if the loop didn't break -> all 3 answers are wrong
            print(f"{a} + {b} = {result}")

    print("Score:", score)



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                raise ValueError
            else:
                return level

        except ValueError:
            pass


def generate_integer(level):

    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()