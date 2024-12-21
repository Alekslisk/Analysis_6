# # def funcA():
# #     return 5

# # def fibbonachi(n: int) -> int:
# #     """
# #     Функция для вычисления последовательности фибоначи
# #     """
# #     if n == 0:
# #         return 0
# #     if n == 1 or n == 2:
# #         return 1
# #     prev_num = 0
# #     now_num = 1
# #     for _ in range(2, n + 1):
# #         prev_num, now_num = now_num, prev_num + now_num
    
# #     return now_num 

# # print(fibbonachi(4))

# # Рекурсия - вызов функцией самой себя

# # Опасность: бесконечный цикл
# # 1. Базовый случай(условие выхода)
# # 2. Рекурсивный случай

# def fibbonachi_no_cash(n):
#     global cnt_n
#     cnt_n += 1
#     if n == 0 or n == 1:
#         return 1
#     return fibbonachi_no_cash(n - 1) + fibbonachi_no_cash(n - 2)


# def fibbonachi(n):
#     global cnt
#     cnt += 1
#     if n not in cash:
#         cash[n] = fibbonachi(n - 1) + fibbonachi(n - 2)
#     return cash[n]

# cnt_n = 0
# cnt = 0
# cash = {0:1, 1:1}

# print(fibbonachi_no_cash(30))
# print(cnt_n)

# print(fibbonachi(30))
# print(cnt)



# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)

# cash_fact = {0:1}

# def factorial(n):
#     if n not in cash_fact:
#         cash_fact[n] = n * factorial(n - 1)
#     return cash_fact[n]

# Декораторы
# Обертка для функций

# def decorator(old_func):
#     def new_func():
#         return old_func
    
#     return new_func

# @decorator
# def func():
#     return 1



# def count(f):
#     total = 0

#     def decorated(*arg, **kwargs):
#         nonlocal total
#         total += 1
#         return f(*arg, **kwargs), total
    
#     return decorated

# @count
# def fibbonachi(n: int) -> int:
#     """
#     Функция для вычисления последовательности фибоначи
#     """
#     if n == 0:
#         return 0
#     if n == 1 or n == 2:
#         return 1
#     prev_num = 0
#     now_num = 1
#     for _ in range(2, n + 1):
#         prev_num, now_num = now_num, prev_num + now_num
#     return now_num

# print(fibbonachi(10))

# print(fibbonachi(20))

# print(fibbonachi(30))

# Генераторы
# вместо return -> yield

gen = (i for i in range(10))

def fib(n):
    n_1, n_2 = 1, 1
    for i in range(n):
        yield n_1
        n_1, n_2 = n_2, n_1 + n_2



def my_range(start=1, n=1, step=1):
    cnt = start
    while cnt <= n:
        yield cnt
        cnt += step

def fact(n):
    n_p = 1
    for i in my_range(2, n + 1):
        yield n_p 
        n_p *= i
        

print(list(my_range(n = 5)))

print(list(fact(5)))
