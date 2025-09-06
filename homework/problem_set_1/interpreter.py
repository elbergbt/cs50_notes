# x y z
# x z - numbers
# y = + - * /

def main():
    exp = input("Expression: ")
    print(interpreter(exp))

def interpreter(n):
    x, y, z = n.split()
    x = float(x)
    z = float(z)

    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z
        case _:
            return False

main()
