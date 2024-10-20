for i in range(4):
    name = input("Enter your name: ")

    with open("names.txt", "a") as file:
        file.write(f"{name}\n")

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(f"hello, {line}")




import sys
from sys import argv


def main():

    filename = argv[1]
    if check(filename) == True:


def check(name):

    if len(name) == 1: and argv[1].endswith(".py")
        return True
    else:
        sys.exit("non-zero exit code")

def count():
    try:
        with open(argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit()

    loc = 0

    for line in lines:
        if line.startswith("#") or line.isspace():
            continue
        else:
            loc += 1
    return loc

if __name__ == "__main__":
    main()