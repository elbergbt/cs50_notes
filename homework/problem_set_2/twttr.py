# Input: Twitter
# Output: Twttr
#A, E, I, O, and U

def main():
    message = input("Input: ")
    result = twttr_convert(message)
    print("Output:" , result)

def twttr_convert(text):
    ms = []
    for i in range(len(text)):
        if text[i] not in "aeiouAEIOU":
            ms.append(text[i])
    return "".join(ms)

main()

