def main():                               # this function prints the value
    fraction = input("fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):           # this function prompts the user for a fraction and re-prompts errors mentioned above happen.
    while True:
        try:
            numerator, denominator = fraction.split("/")
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            f = new_numerator / new_denominator
            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fraction = input("fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):       # this function calculated the percentage and returns the value

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return F"{percentage}%"


if __name__ == "__main__":
    main()
