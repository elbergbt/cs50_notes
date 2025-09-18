import sys

# var 1
# python sys_lib.py _ <- place for name/sys.argv[1]
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])

# var 2
if len(sys.argv) < 2:
    sys.exit("Too few argument")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)

# Input: python sys_lib.py David Marco Ronald
# Output:
# Hello, my name is David
# Hello, my name is Marco
# Hello, my name is Ronald