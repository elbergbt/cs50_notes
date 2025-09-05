#

def main():
    a = input()
    print(convert(a))

def convert(t = ":)"):
    return t.replace(":)", "🙂").replace(":(", "🙁")

main()