c = 300000000

def main():
    m = int(input("Input mass in kilograms "))
    print(f"E = mc^2, where mass = {m} kg, E =", formula(m))

def formula(mass: int):
    return mass * (pow(c,2))

main()