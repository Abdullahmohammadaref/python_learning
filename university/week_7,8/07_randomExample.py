#!/usr/bin/env python3

"""
Examples for random numbers, numpy and csv

https://docs.python.org/3/library/random.html
https://docs.python.org/3/library/csv.html
https://numpy.org/

Prof. Dr. Sami Alsalamin, 2024, sami.alslamin@gisma.com
"""

import random

random.seed(34) # Set the seed for the RNG

sequence = ["Apple", "Pear", "Peach", "Pineapple"]

print("Random integer between 1 and 10:", random.randint(1,10))
print("A random fruit:", random.choice(sequence))
print("A float between 0 and 1:", random.random())
print("Gaussian distribution with mu=0 and sigma=1:", random.gauss(0,1))

print("Items:", sequence)
random.shuffle(sequence)
print("Shuffled items:", sequence)

print("3 random elements out of the sequence:", random.sample(sequence,3))

############
# select a random character from a string
import random

name = 'pynative'
char = random.choice(name)
print("random char is ", char)

# select a random number from a list
import random
numbers = [1, 2, 3, 4, 5]
number = random.choice(numbers)
print("random number is ", number)

#######
# shuffle a list
a =[1,2,3,4,5]
random.shuffle(a)
print(a)
###############################################################################
# install numpy first   
import numpy as np

# Array with 100 random numbers
someNumbers = np.random.random(100)

print("Some random numbers", someNumbers)

print("Sum", np.sum(someNumbers))
print("Min", np.min(someNumbers))
print("Max", np.max(someNumbers))
print("Mean", np.mean(someNumbers))
print("Median", np.median(someNumbers))

# Get 31 values between 1 and 5, evenly spaced:
print(np.linspace(1,5, num=31))

# Get Values from 0 to 10 with a step size of 0.1
print(np.arange(0, 10, 0.1))

# Some more examples
print(np.pi)
print(np.sqrt(16))

###################################################################################################


# What to try out
#################
# - Create a list of greetings and write a function which randomly greets a
# person with a given name
import random

def random_greeting(name, greeting):
    random_greeting = random.choice(greetings)
    return f"{random_greeting} {name}"

def main():
    greetings = ["Hello", "Hello, how are you", "yoooo", "wazaaaaaaaaaaaaaaaaa"]
    name = input("What is your name? ")
    print(random_greeting(name, greetings))

if __name__ == "__main__":
    main()

# - Create a list of numbers and use the random module to shuffle the list

numbers = [1, 2, 3, 4, 5]

print(random.shuffle(numbers))

# - Create a list of numbers and use the random module to randomly select
# a number from the list

numbers = [1, 2, 3, 4, 5]
print(random.choice(numbers))

# - Create a sccript that generate a 100 random password including numbers and chars and save values in CSV file

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
