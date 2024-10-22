import sys
import csv


from sys import argv


def main():

    students_list = file_reader(check())
    file_writer(students_list)
    print(students_list)
def check():

    if len(sys.argv) == 3 and argv[1].endswith(".csv") and argv[2].endswith(".csv"):
        return str(argv[1])
    else:
        sys.exit(" wrong number of arguments or file doesn't end with .csv")

def file_reader(name):

    students = []
    try:
        with open(name, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                last, first = row["name"].split(", ")
                students.append({"first": first, "last": last, "house": row["house"]})
            return students

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

def file_writer(name):

    with open(argv[2], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in name:
            writer.writerow(row)

if __name__ == '__main__':
    main()