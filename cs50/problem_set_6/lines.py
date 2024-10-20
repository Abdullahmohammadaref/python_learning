import sys
from sys import argv


if len(sys.argv) == 2 and argv[1].endswith(".py"):
    filename = str(argv[1])
else:
    sys.exit("non-zero exit code")

try:
    with open(filename, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit()

loc = 0

for line in lines:

    if line.isspace():
        continue
    line = line.lstrip()
    if line.startswith("#"):
        continue
    else:
        loc += 1
print(loc)
