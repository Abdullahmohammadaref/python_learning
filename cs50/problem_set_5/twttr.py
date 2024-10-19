# this program remve vowl letters


def main():   # this function call the convert function output and prints the result
    input_with_vowel = input("input: ")
    output_withought_vowel = shorten(input_with_vowel)
    print("output:", output_withought_vowel)

def shorten(word): # this function ask the user for an input and the it deletes vowl letters
    output = ""    # a list where letters will be inserted except voles
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]  # a list that specify what are the vowl leters
    for c in word:  # this loop goes through the letters one by one.
        if c in vowels:
            output += ""  # if the letter is vowl then it doesnt insert anything and moves to the next letter
        else:
            output += c  # if the letter is not a vowl then it inserts the letter and moves to the next letter
    return f"{output}"

if __name__ == "__main__":
    main()