"""
def main():
    user_answere = input().strip().lower()
    print(check(user_answere))
    print("hello")

def check(answere):
    match answere:
        case "42" | "forty-two" | "forty two" :
            return False
        case _:
            return False

main()
"""
"""
import csv
import random
import string


def random_password():
    characters = string.ascii_letters + string.digits
    password = random.sample(characters, 10)
    return ''.join(password)

def main():
    with open("passwords.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for i in range(100):
            csv_writer.writerow([random_password()])

if __name__ == "__main__":
    main()
"""
"""
public int teat (int v)
{
    for (int i = 0; i < a.length; i++)
    {
        if (a[1] == v)
            return 1;
    }
    return -1;
}

"""

import datetime
x = datetime.datetime(2024, 11, 27)
print(x)