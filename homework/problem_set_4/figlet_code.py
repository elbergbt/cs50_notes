import random

import pyfiglet
import sys


user_input = input("Input: ")

fig = pyfiglet.Figlet()
font_names = fig.getFonts()
random_font = random.choice(font_names)

# zero position is a file name, so the length is == 1
if len(sys.argv) == 1:
    fig.setFont(font=random_font)
    print(f"Output: {fig.renderText(user_input)}")
elif len(sys.argv) == 3:
    if sys.argv[1] not in ("-f", "--font") or sys.argv[2] not in font_names:
        sys.exit("Invalid usage")
    else:
        fig.setFont(font=sys.argv[2])
        print(f"Output: {fig.renderText(user_input)}")
else:
    sys.exit("Invalid usage")

