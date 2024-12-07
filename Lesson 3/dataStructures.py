# int, bool, str, float

# a = 1

# print(a)

# a = 2

# print(a)

# list, tuple, set, dict

my_list = [] #list

my_tuple = () #tuple

my_set = set()

my_dict = {} # dict()


my_list.append([1,2])
my_list.append([3,4])
my_list.append([5,6])


# list = tuple, но tuple нельзя изменять
print('Часть про tuple:')
my_tuple = tuple(my_list)

print(my_tuple)

#index, это координаты ячейки

print(my_list[0])
print(my_tuple[0])

my_list[0] = [15,13,12] # 0=>15, 1=>13, 2=>12

print(my_list)

#my_tuple[0] = [15,13,12], нельзя менять и добавлять элементы


my_tuple[0][1] = 10

print(my_tuple)


# Set, множество
print('Часть про множества:')
my_set.add(1)
my_set.add(1)
my_set.add(2)
my_set.add(1)
my_set.add(3)

my_set_2 = {1,3,5}

print(my_set)
print(my_set_2)
print(f'difference множеств {my_set - my_set_2}')
print(f'union множеств {my_set | my_set_2}')
print(f'intersection множеств {my_set & my_set_2}')
print(f'sym difference множеств {my_set ^ my_set_2}')

# dict, map, hashmap
print('Часть про dictionary:')

my_dict['a1'] = [1,2,3,4]
my_dict['want_set'] = {1,2,3,4,1,1,2}
my_dict['just'] = 1
my_dict[0] = 'Могу'

print(my_dict)

print(my_dict[0])

print(my_dict['want_set'])

my_dict_2 = {'apple': 100, 'orange':200, 'pineapple':1000}
print(my_dict_2, f'type: {type(my_dict_2)}')

my_set_by_brackets = {1,1,1,1,1,1}
print(my_set_by_brackets, f'type: {type(my_set_by_brackets)}')