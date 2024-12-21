# my_list = []

# for i in range(5):
#     if i % 2 == 0:
#         my_list.append(i)

# print(my_list)

# my_list = [i for i in range(10 ** 7) ]

# import sys

# print(sys.getsizeof(i for i in range(10 ** 7)))

# print(sys.getsizeof(my_list))


# my_list = [i for i in range(10 ** 7) ]

# import sys
# import time

# # %%time
# print('Я спать')
# time.sleep(10)
# print('Я проснулься')
# # print([i for i in range(10 ** 7) ])

# print(sys.getsizeof(my_list))

# numbers = (1,1,1,1, 2, 2, 2, 10 , 100 ,1 )

# my_set = {i for i in numbers}

# print(my_set)

# my_dict = {key: value for key, value in enumerate(range(10))}
# print(my_dict)


numbers = {1, 2, 3, 4, 5}

dividers = {number: [i for i in range(1, number + 1) if number % i == 0] for number in numbers}
print(dividers)


my_dict = {value: key + 1 for key , value in enumerate(['A','B','C'])}
print(my_dict)
print(my_dict['A'])

