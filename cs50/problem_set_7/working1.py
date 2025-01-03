import re


def main():
    print(convert(input("Hours: ")))


def convert(s):

        matches = re.fullmatch(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
        result = s
        if matches:
                parts = matches.groups()
                if int(parts[1]) > 12 or int(parts[5]) > 12:
                    raise ValueError("make sure that the hours are not greater than 12 and the minutes are not greater than 59")
                hours, minutes, meridian = parts[1], parts[2], parts[3]
                if meridian == "PM":
                    if int(hours) == 12:
                        result = 12
                    else:
                        result = int(hours) + 12

                else:
                        result = s.replace(hours, str(int(hours) + 12)).replace(meridian, "")
                        continue
            return result
        else:
            raise ValueError("no match")



if __name__ == "__main__":
    main()