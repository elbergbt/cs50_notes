import os
import sys

def main():

   if len(sys.argv) == 2:
      filename = sys.argv[1]

      if not is_python_file(filename):
          sys.exit("Not a Python file")
      if not file_exist(filename):
          sys.exit("File does not exist")

      print(f"In the file {filename}, there are {code_lines(filename)} lines of code")

   elif len(sys.argv) > 2:
       sys.exit("Too many command-line arguments")
   else:
       sys.exit("Too few command-line arguments")


def file_exist(filename):
    return os.path.isfile(filename)


def is_python_file(filename):
    return filename.endswith(".py")

def code_lines(filename):
    count = 0
    with open(filename, "r") as file:
        context = file.readlines()
        for row in context:
            if row.startswith("#") or (row.strip() == ""):
                count += 0
            else:
                count += 1
    return count

if __name__ == "__main__":
    main()

