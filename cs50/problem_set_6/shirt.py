import os
import sys
import PIL


from sys import argv
from PIL import Image, ImageOps

def main():

    image_before, image_after, cs50_shirt_image = str(argv[1]).lower(), str(argv[2]).lower(), "shirt.png"
    wear_tshirt(image_before, image_after, cs50_shirt_image)

def wear_tshirt(before, after, shirt):

    if len(argv) != 3:

        sys.exit("number of inputs are not equal to 2")

    extension = ["png", "jpg", "jpeg"]
    before_format = sys.argv[1].split(".")
    after_format = sys.argv[2].split(".")
    before_extension = before_format[1]
    after_extension = after_format[1]

    if before_extension not in extension or after_extension not in extension:

        sys.exit(f"input and output file names should end with png, jpg, or jpeg")

    elif before_extension != after_extension:

        sys.exit("both input and output file names should have the same file extension")

    else:

        try:

            before_image = Image.open(before)
            shirt = Image.open(shirt)
            size = shirt.size
            after_image = ImageOps.fit(before_image, size)
            after_image.paste(shirt, shirt)
            after_image.save(after)

        except FileNotFoundError:

            sys.exit("input file doesn't exist")

if __name__ == '__main__':
    main()