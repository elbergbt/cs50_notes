def main():
    message = input("Input: ")
    result = shorten(message)
    print("Output:" , result)

def shorten(word):
    ms = []
    word = word.lower().strip()
    for i in range(len(word)):
        if word[i] not in "aeiouAEIOU":
            ms.append(word[i])
    return "".join(ms)

if __name__ == "__main__":
    main()