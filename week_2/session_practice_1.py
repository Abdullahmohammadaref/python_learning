my_list = ['one', 2, 'three', [1, 2, 3, 4, 5], 5]
my_tuple = ('one', 2, 'three', (1, 2, 3, 4, 5), 5)
my_set = {'one', 2, 'three', 5}

my_list.append(6)
my_tuple += (6,)
my_set.add('six')

print(my_list)
print(my_tuple)
print(my_set)

my_list.pop(1)
my_tuple = my_tuple[:1] + my_tuple[2:]
my_set.remove(5)

print(my_list)
print(my_tuple)
print(my_set)

my_list[1] = 12
my_tuple = my_tuple[:1] + (12,) + my_tuple[2:]
my_set.remove('six')
my_set.add(12)

print(my_list)
print(my_tuple)
print(my_set)

