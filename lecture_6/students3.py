# reads a CSV file into a list of dict objects, creating empty dict first

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # student = {}
        # student["name"] = name
        # student["house"] = house

        # student = {"name": name, "house": house}
        # students.append(student)
        
        students.append({"name": name, "house": house})

for student in students:
     print(f"{student['name']} is in {student['house']}")