def main():
    jj = input()
    jj = convert_to_snake(jj)
    jj = convert_to_lower(jj)
    print(''.join(jj))  # if jj = ['H', 'e', 'l', 'l', 'o'] then "Hello"

#convert camel case to snake case

def convert_to_snake(user_input):
    result = []
    for i, ch in enumerate(user_input):
        if ch.isupper() and i > 0:
            result += "_" + ch
        else:
            result += ch
    return result

#conver capital letters to lowercase

def convert_to_lower(h):
    for i in range(len(h)):
        if h[i].isupper:
            h[i] = h[i].lower()
    return h

main()
