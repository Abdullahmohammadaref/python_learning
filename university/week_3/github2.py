#!/usr/bin/env python3

"""
Examples for loops

https://docs.python.org/3/reference/compound_stmts.html#for
https://docs.python.org/3/reference/compound_stmts.html#while

Sami Alsalamin, 2024, sami.alsalamin@gisma.com
"""
from xml.dom.minidom import ProcessingInstruction

# Print numbers from 1 to 10
print("For loop")
for number in range(1,11):
    print(number)

# Print numbers from 1 to 10 but break loop under certain conditions
print("Break loop")
for number in range(1,11):
    if number == 5:
        break # Stop the loop
    print(number)

# Print numbers from 1 to 10 but continue loop under certain conditions
print("Continue loop")
for number in range(1,11):
    if number % 2: # Modulo operator: %
        continue # Next iteration
    print(number)

# Iterate over items
print("Iterate loop")
items = ["Book", "Banana", "Computer"]
for item in items:
    print("I will take my", item, "with me...")

# While loop
print("While loop")
number = 1
while (number < 10):
    print(number)
    number += 1 # Short form for number = number + 1, number++ does not exist

# What to try out
#################
# 1 - Read a string from the user, and Print characters present at an even index number
#  E.g., Hello world, the output (H, l o w r d)

text = str(input())
no_char = len(text)

for i in range(0, no_char, 2):
    print(text[i], end="")


# 2 - Write a Python code to remove characters from a string from 0 to n and print the new string
# Hint, Use string slicing to get a substring. For example, remove the first four characters using s[4:]

test = "test text"
test = test[4:]
print(test)

# 3 - Find the number of occurrences of a substring in a string
# Hint, Use string method count(). E.g., s.count("something")

test = "test text"
letter = "t"
print(test.count(letter))

# 4 - Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after
# reverse. For example, 545 is the palindrome number.
# Hint,Reverse the given number and save it in a different variable. Use the if condition to check if the original and
# reverse numbers are identical.

initial_number = "454"
no_elements = len(initial_number)
reversed_number = ""

for i in range(0, no_elements):
    reversed_number = f"{initial_number[i]}{reversed_number}"

if reversed_number == initial_number:

    print(f"{initial_number} is palindrome")

else:

    print(f"{initial_number} is not palindrome")


# 5 - Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.
# Hints,
# Create an empty list named result_list
# Iterate the first list using a for loop
# In each iteration check if the current number is odd using the num % 2 != 0 formula. If the current number is odd, add it to the result list
# Now, Iterate the second list using a loop.
# In each iteration check if the current number is even using the num % 2 == 0 formula. If the current number is even, add it to the result list.
# Print the result list.


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result_list = []
for item in list1:
    if item % 2 != 0:
        result_list.append(item)
    else:
        continue
for item in list2:
    if item % 2 == 0:
        result_list.append(item)
    else:
        continue

print(result_list)



# 6 - You can user several loops. Write a program which outputs a multiplication
# table from 1 to 100 (1x1=1, 1x2=2, etc.)

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i}x{j}={i * j} ", end="")
    print("")


    ### or

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i}x{j}={i * j} ", end="")


