import tabulate
import sys


from tabulate import tabulate
from sys import argv
from csv import reader

def main():

    filename = check(argv[1])
    menu_list = file_reader(filename)
    print(tabulate(menu_list, headers='firstrow', tablefmt='grid'))

def check(name):

    if len(sys.argv) == 2 and name.endswith(".csv"):
        return str(name)
    else:
        sys.exit("non-zero exit code")

def file_reader(name):

    try:
        with open(name, "r") as file:
            return reader(file.readlines())
    except FileNotFoundError:
        sys.exit("non-zero exit code")

if __name__ == "__main__":
    main()
