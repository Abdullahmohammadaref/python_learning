import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        match = re.search("^([0-9]{1,2}):?([0-9]{2})? (AM|PM)$", s)
        for match in s:
            if int(match.group(0)) > 12 or int(match.group(1)) > 59:
                raise ValueError
            elif match.group(2) == "AM":
                if int(match.group(0)) = 12:
                    result = s.replace(match.group(0), "00")
            elif match.group(2) == "PM":
                ...

    except ValueError("make sure that the hours are not greater than 12 and the minutes are not greater than 59"):
        return


if __name__ == "__main__":
    main()


#^([0-9]{1,2}):?([0-9]{2})? AM to $