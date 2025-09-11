# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate;
# they must come at the end. For example, AAA222 would be an acceptable …
# vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# done “No periods, spaces, or punctuation marks are allowed.”

#CS50

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):

    if is_two_letters(s) and is_characters(s) and is_max_min(s) and num_location(s):
        return True
    else:
        return False


def num_location(st):
    for i in range(len(st)):
        if st[i].isdigit():  # check if it is digit
            if st[i] == "0":
                return False
            return st[i:].isdigit()
    return True



def is_max_min(st):
    if 2 <= len(st) <= 6:
        return True
    else:
        return False


def is_two_letters(letters):
    if is_max_min(letters):
        if letters[0].isalpha() and letters[1].isalpha():  # .isalpha check if it is letter
            return True
        else:
            return False
    else:
        return False


def is_characters(ch):
    for i in range(len(ch)):
        if not ch[i].isalnum(): #isalnum() allow only characters and numbers
            return False
    return True

main()