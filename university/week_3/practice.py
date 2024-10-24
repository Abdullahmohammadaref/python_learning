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