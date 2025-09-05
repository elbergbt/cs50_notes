# if / and

score  = int(input("Score: "))

if score >= 90 and score <=100:
    print("Grade: A")
elif score >=80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade is C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

#simpler version 1

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade is C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

#simpler version 2

if score >= 90 :
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade is C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
