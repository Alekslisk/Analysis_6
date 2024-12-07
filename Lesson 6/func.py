# def обявление функций
# return возвращает значение
# return -> являеться финальным оператором

# def my_sum( a, b):
#     return a + b


# a = int(input())

# b = int(input())

# c = my_sum(a, b)

# print(f"C = {c}")


# Области видимости
# def is_prostoe(num):
#     if num == 1:
#         return False
#     if num == 2:
#         return True

#     for i in range(2,num):
#         if num % i == 0:
#             return False
        
#     return True


# num = int(input())

# if is_prostoe(num):
#     print('Число простое')
# else:
#     print('Число не простое')



def srez( nums, a = None, b = None, step = 1):
    if not b:
        b = len(nums)
    if not a:
        a = 0
    return nums[a:b:step]

my_list = [1,2,3,4,5,6,7]

print(srez(my_list))