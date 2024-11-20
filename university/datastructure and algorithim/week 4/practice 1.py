import numpy as np
import cv2
import matplotlib.pyplot as plt
"""
def main():
    array = np.array([1,2,3,4,5,100])
    print(max(array))

def max(array):
    max_value = array[0]
    for element in array:
        if element > max_value:
            max_value = element
    return max_value

if __name__ == '__main__':
    main()
"""
"""
import numpy as np
array = np.array([1,2,3,4,5,100])
max_value = np.max(array)
print(max_value)
"""
"""
def main():
    array = np.array([1,2,3,
                      4,5,6,
                      7,8,9])
    print(array_reshape_to_3x3(array)[0, 1])

def array_reshape_to_3x3(array):
    new_array = np.reshape(array, (3, 3))
    return new_array

if __name__ == '__main__':
    main()
"""
""""
def main():
    array = np.array([1,2,3])
    item = int(input("Enter an integer: "))
    print(add_item_at_begenning(array, item))

def add_item_at_begenning(array, item):
    final_array = np.array([item])
    for element in array:
        final_array = np.append(final_array, element)
    return final_array

if __name__ == '__main__':
    main()
"""
"""
array = np.array([1,2,3,4,5])
updated_array = np.insert(array, 3, 100)
print(updated_array)
"""
""""
image = cv2.imread('lisa.png')
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.show()
"""
