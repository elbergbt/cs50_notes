# sorts a list of dicts using a function

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({'name': name, 'house': house})

def get_name(student):
    return student['name']

for student in sorted(students, key=get_name): # key expects a function (get_name or lambda), not a value
    print(f"{student['name']} is in {student['house']}")

# sort a list of dicts using lambda function

for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} is in {student['house']}")