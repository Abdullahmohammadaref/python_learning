counting sort mk:
import numpy as np

original_array = np.array([9, 5, 2, 4, 2, 8, 5], dtype = int)

count_array = np.zeros(np.max(original_array) + 1, dtype=int) #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for number in original_array: #[0, 0, 2, 0, 1, 2, 0, 0, 1, 1]
    count_array[number] += 1

increment_array = np.array([], dtype=int)
total = 0
index = 0
for number in (count_array):  # [0 0 2 0 3 5 0 0 6 7]
    if number <= 0:
        increment_array = np.append(increment_array, 0)
        index += 1
        continue
    else:
        increment_array = np.append(increment_array, number + total)
        total += count_array[index]
        index += 1

sorted_array = np.zeros_like(original_array) #[0, 0, 0, 0, 0, 0, 0]
for number in original_array:
    increment_array[number] -= 1
    sorted_array[increment_array[number]] = number

print(sorted_array)


