import sys
import csv
import os



def main():
    if len(sys.argv) == 3:
        filename_before = sys.argv[1]
        filename_after = sys.argv[2]

        if not is_exist(filename_before):
            sys.exit("File does not exist")
        if not is_csv(filename_before):
            sys.exit("Not a CSV file")

        # read and transform data
        students = []
        with open(filename_before, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row['name'].split(", ")
                students.append({
                    'first': first,
                    'last': last,
                    'house': row['house']
                })
        # write new CSV
        with open(filename_after, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            writer.writerows(students)



    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


def is_exist(filename):
    return os.path.isfile(filename)

def is_csv(filename):
    return filename.endswith(".csv")



if __name__ == "__main__":
    main()