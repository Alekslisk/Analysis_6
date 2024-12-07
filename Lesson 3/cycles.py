# # постфиксный(while), префиксный(do while)| в питоне не реализован
# # Параметрический(for)

# print('Часть по while:')

# a = int(input('введите число: '))
# while a >= 5: #if
#     print(f'a на данный момент равен {a}')
#     a -= 1


# sum = 0

# while True:
#     n = int(input('Введите число для суммирования или 0 для остановки: '))
#     sum += n
#     if n == 0:
#         break # break - прекращает текущий цикл
# print(sum)

# print('While + массивы: ')

# my_list = []

# while len(my_list) <= 5:
#     my_list.append(int(input()))


# n = 0
# while n < len(my_list):
#     print(f'index:{n} value:{my_list[n]}')
#     n += 1

# print(my_list)

# print("Предисловие \n Функция Range:")

# print(range(10))

# for i in range(1,10,3):
#     print(i, end = ' ')

# n = int(input('\n'))
# list_for = []

# for i in range(n):
#     list_for.append(int(input()))

# print('\nС помошью индекса')
# for i in range(len(list_for)):
#     print(list_for[i], end = ' ')
# print('\nС помошью for(без индекса)')
# for i in list_for:
#     print(i,end = ' ')

# print('\n',list_for)

# cnt = 0
# while True:
#     say = input()
#     if say == 'Приехали!':
#         break
#     for i in say.split():
#         if i == 'зайка':
#             cnt += 1
# print(cnt)


# if ?:
#     for i in range(1,10 + 1):
#         print(i, end = ' ')
# else:
#     for i in range(10,1 - 1,-1):
#         print(i, end = ' ')