import re


def main():
    print(convert(input("Hours: ")))


def convert(s):

    try:
        matches = re.finditer(r"([0-9]{1,2}):?([0-9]{2})?( AM|PM)", s)
        result = s
        if matches:
            for match in matches:
                hours, minutes, meridian = match.groups()
                if int(hours) > 12:
                    raise ValueError("make sure that the hours are not greater than 12 and the minutes are not greater than 59")
                elif meridian == "AM":
                    if int(hours) == 12:
                        result = s.replace(hours, "00").strip(meridian)
                        continue
                    else:
                        result = s.strip(meridian)
                        continue
                elif meridian == "PM":
                    if int(hours) == 12:
                        result = s.strip(meridian)
                        continue
                    else:
                        result = s.replace(hours, str(int(hours) + 12)).strip(meridian)
                        continue
            return result
        else:
            raise ValueError("no match")
    except ValueError as e:
        return e


if __name__ == "__main__":
    main()