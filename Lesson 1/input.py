name = input('Введите свое имя: ')

print(f'Приветсвую вас {name}')

a = int(input("введите первое число: "))

b = int(input("введите второе число: "))

# # # Арифметические операций
# # # + - * / // %
print(f"a + b = {a+b}")

print(f"a - b = {a-b}")

print(f"a / b = {a/b}")

print(f"a * b = {a*b}")

print("a // b =", a//b) # Целое от деления

print("a % b =", a%b) # Остаток от деления

# # Логические операций
# # > < == != >= <=

# print('a > b',a > b)

# print('a < b',a < b)

# print('a >= b',a >= b)

# print('a <= b',a <= b)

# print('a == b',a == b)

# print('a != b',a != b)


# and or not
a = bool(input("Введите выражение: "))
b = bool(input("Введите выражение: "))

print(f"a and b = {a and b}")
print(f"a or b = {a or b}")
print(f"a = {a} , !a = {not a}")
print(f"b = {b} , !b = {not b}")