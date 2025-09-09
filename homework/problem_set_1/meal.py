def main():
    time = input("What time is it? ")
    time = convert(time)
    if   7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")




def convert(time):
    if "p.m." in time or "a.m." in time:
        time, period = time.split()
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

        if period == "a.m.":
            if hours == 12:
                hours = 0
        elif period == "p.m.":
            if hours != 12:
                hours += 12

    else:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

    return hours + minutes/60


if __name__ == "__main__":
    main()