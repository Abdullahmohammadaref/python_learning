import datetime
import sys

class Person:

    def __init__(self, name, age, date):
        self.name = name
        self.age = age
        self.date = date

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Date: {self.date}"

def main():
    persons = []
    while True:
        try:
            print("Input process started")
            name = input("Name: ")
            if not name.isalpha():
                raise ValueError("Name must only contain letters and spaces")
            age = int(input("Age: "))
            if age < 0:
                raise ValueError("Age should be a number greater than 0.")
            date = datetime.datetime.now()
            person = Person(name, age, date)
            persons.append(person)
            print("person added sucessfully")
        except KeyboardInterrupt:
            print("\npersons:")
            for person in persons:
                print(f"-{person}")
            sys.exit()
        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == '__main__':
    main()