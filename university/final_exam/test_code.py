# q1

import datetime
from datetime import date

from IPython.external.qt_loaders import QT_API_PYQT5

my_birthday = input("enter your birthday: ")  # stores the birthday input from the user in a dd.mm.yyyy format.
day, month, year = my_birthday.split(".") # stores the day, month, and year each as individual variable from the my_birthday variable that the user have entered using a split to show which parts of the string my_birthday should be assigned for each value

my_birthday =datetime.date(int(year), int(month), int(day)) # create a date object using the datetime library and converting the previous day, mont, year values into integers.

today = date.today() # story today date using the datetime library in a today variable.

days_lived = today - my_birthday    # calculating how many days are between today and the inputed birthday, then storing them in a days_lived variable.

print(days_lived.days)  # printing howmany days lived. and using the datetime "days" function to only print the days.

Q2

user_input = input("input a word: ")   # store the word inputed by the user in a user_input variable.

if user_input == user_input[::-1]:    # This if statement checks weather the user_input is the same as the reversed user_input. It prints "The word is palindrome" if it is the same, and it prints "The word is not palindrome" if it is not the same.
    print("The word is palindrome")
else:
    print("The word is not palindrome")

Q3


def word_counter(sentence):
    """
    This function takes a string as an input.
    Then is changes all the letter cases in that string to lower case, and it splits the string into words.

    after that it defines a local variable called length that stores the number of words in  that string

    after that it creates and stores a dictionary in a frequency_of_words local variable. this dictionary is then filled with all the words in the input string and the number of times each word have been repeated inside that string

    after that is stores the word with the highest frequency count into the most_frequent_words local variable.

    Finally it returns all these local variables (length, most_frequent_word, frequency_of_words) in one list.
    """
    sentence = sentence.lower().split(" ")
    length = len(sentence)

    frequency_of_words = {}
    for word in sentence:
        if word in frequency_of_words:
            frequency_of_words[word] += 1
        elif word not in frequency_of_words:
            frequency_of_words[word] = 1

    most_frequent_word = max(frequency_of_words, key=frequency_of_words.get)

    return [length, most_frequent_word, frequency_of_words]


def main():
    input_text = "Write a Python script that counts the number of words in a string and find the most frequent one. This question is part of the Python exam. Your Python script does not care about letter cases. Good luck!"  # storing the testing text into a input_text variable.
    output = word_counter(input_text)  # calling the word_counter function and giving it the input_text variable

    print(
        f"Number of words: {output[0]}")  # this prints the first item in the returned list which is the number of words in the input_text
    print(
        f"Most frequent word: {output[1]}")  # This prints the second item in the returnd list which is the most repeated word in the input_text variable
    for word in output[
        2]:  # this loop prints the third item in the list. this item is a dictionary that contains the words and their relative count. So this loop will print both of these values for every word in the list
        print(f"number of occurrences of {word}: {output[2][word]}")


if __name__ == "__main__":  # the main() function will be called only if the function is at the start of the program
    main()

Q4

import random


def random_fruit_selector(fruits):
    """
    This function takes the list of fruits as a input.

    I then uses the random.choices library method to select a random fruit from the list according to the probability of each fruit

    finally the selected fruit is returned
    """

    next_word = random.(list(fruits.keys()), weights=fruits.values())

    return next_word


def main():
    items = {  # stores the items of the dictinary in a list variable called items
        'apple': 0.1,
        'banana': 0.3,
        'cherry': 0.2,
        'date': 0.4
    }

    random_fruit = random_fruit_selector(
        items)  # calling the random_fruit_selector function and giving it the items dictionary variable

    print(random_fruit)  # printing the returned fruit from the random_fruit_selector function


if __name__ == "__main__":  # the main() function will be called only if the function is at the start of the program
    main()

Q5


class Car:
    def __init__(self, make, model, year, odometer_reading):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def get_description(self):
        return f"{self.make}, {self.model}, {self.year}, {self.odometer_reading}"


    def read_odometer(self):
        return self.odometer_reading

    def update_odometer(self, milage):
        if milage > self.odometer_reading:
            self.odometer_reading = milage


class CarOwner:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_owner_info(self):
        return f"-{self.name}, {self.address}"


class RegistrationDepartment():

    def __init__(self, registrations):
        self.registrations = {}

    def register_car(self, car, owner):
        self.registrations.update({car: owner})
    def get_registration_info(self,car):
        return self.registrations.get(car)

    def add_owner_car(self, owner, car):
        ...

    def delete_owner_car(self, owner,car):
        ...


def main():
    owner1 = CarOwner("Abdullah", "street 1")
    owner2 = CarOwner("khaled", "street 2")
    owner3 = CarOwner("jamal", "street 3")
    owner4 = CarOwner("ahmad", "street 5")

    car1 = Car("kia", "jeep", 2005, 3000)
    car2 = Car("ford", "focus", 2003, 4000)
    car3 = Car("dodge", "chrger", 2010, 5000)
    car4 = Car("tesla", "model s", 2024, 6000)

    department1 = RegistrationDepartment({car1: owner1, car2: owner2, car3: owner3, car4: owner4})


    print(Car.get_description(car1))
    print(Car.get_description(car2))
    print(Car.get_description(car3))
    print(Car.get_description(car4))

    print(Car.read_odometer(car1))
    print(Car.read_odometer(car2))
    print(Car.read_odometer(car3))
    print(Car.read_odometer(car4))

    print(CarOwner.get_owner_info(owner1))
    print(CarOwner.get_owner_info(owner2))
    print(CarOwner.get_owner_info(owner3))
    print(CarOwner.get_owner_info(owner4))

    print(RegistrationDepartment({car1: owner1, car2: owner2}))


if __name__ == '__main__':
    main()