import cowsay
import sys

if sys.argv == 2:
    cowsay.cow("Hello, " + sys.argv[1])
