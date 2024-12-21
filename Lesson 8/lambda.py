# # lambda

# def my_func(a: int, b: int = 5) -> int:
#     """
#     Моя функция для суммирования
#     :param a: первое число
#     :param b: второе число
#     :return: сумма чисел
#     """
#     return a + b

# help(my_func)

# list_a = [1, 2, 3]

# print(list(map(my_func, list_a)))

# print(list(map(lambda x: x + 5, list_a)))

power = lambda x, y : x ** y

print((lambda x: x % 256)(600))

print(power(2, 3))

numbers_1 = [1,2,3,4]
numbers_2 = [1,2,3,4]

print(list(map(lambda x,y: x * y, numbers_1, numbers_2)))

print(list(filter(lambda x: x > 3, numbers_1)))




# import functools 
# print(functools.reduce(lambda x,y: str(x) + ' ' + y, ['A','B','C'], ''))

# print(functools.reduce(lambda x,y: x + y, [1,2,3,4], 0))

# cum = 0

# cum = cum + 1
# cum += 2
# cum += 3
# cum += 4
# print(cum)


# numbers_1 = [1,2,3,4]
# numbers_2 = [1,2,3]

# print(list(map(lambda x,y: x * y, numbers_1, numbers_2)))
# numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]

# print({i for i in numbers})

# print(sorted({i for i in numbers}))

# print([str(i) for i in sorted({i for i in numbers})])

# print(' - '.join([str(i) for i in sorted({i for i in numbers})]))


# def sum(*nums):
#     result = 0

#     for i in nums:
#         result += i

#     return result

# print(sum(1))

# print(sum(1,2))

# print(sum(1,1,3,45,2,21,34,234,2,31))
    


# def gcd_of_two(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a

# def gcd(*nums):
#     gcd = nums[0]

#     for i in nums:
#         gcd = gcd_of_two(gcd, i)
    
#     return gcd

# def gcd(*nums):
#     gcd = nums[0]

#     for i in nums:
#         while gcd != i:
#             if gcd > i:
#                gcd -= i
#             else:
#                 i -= gcd

#     return gcd

# result = gcd(36, 48, 156, 100500)


# print(result)


# def to_string(*data, sep=' ', end='\n'):
#     return sep.join([str(i) for i in data]) + end

# data = [7, 3, 1, "hello", (1, 2, 3)]
# result = to_string(*data, sep=", ", end="!")

# print(result)

def enter_results(*data):
    global my_data
    for i in data:
        my_data.append(i)


def get_sum():
    global my_data
    filter_even = [x for i, x in enumerate(my_data) if i % 2 == 0 ]
    filter_odd = [x for i, x in enumerate(my_data) if i % 2 != 0 ]
    return (round(sum(filter_odd), 2), round(sum(filter_even), 2))


def get_average():
    global my_data
    filter_even = [x for i, x in enumerate(my_data) if i % 2 == 0 ]
    filter_odd = [x for i, x in enumerate(my_data) if i % 2 != 0 ]
    return (round(sum(filter_odd) / len(filter_odd), 2), round(sum(filter_even) / len(filter_even), 2))

my_data = []

enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())
