from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    print(sing(input("birth date: ")))

def sing(birth_date):
    date_match = re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date)
    if date_match:
        year, month, day = birth_date.split("-")
        date_of_birth = date(int(year), int(month), int(day))
        today_date = date.today()
        days_lived = today_date - date_of_birth
        minutes_lived = days_lived.days * 24 * 60
        minutes_lived_in_words = p.number_to_words(minutes_lived, andword="")
        return f"{minutes_lived_in_words.capitalize()} minutes"
    else:
        sys.exit("Invalid birth date")


if __name__ == "__main__":
    main()