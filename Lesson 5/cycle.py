# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(f"{i * j}")




# for i in range(n):
#     for j in range(n):
#         if i + j <= n:
#             print(j + i + 1, end = ' ')
#     print()


# n = int(input())
# cnt = 1

# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(cnt,end = ' ')
#             cnt += 1
#         if cnt > n:
#             break
#     if cnt > n:
#             break
#     print()

# if i == num or j == num or i == n - num -1 or j == n- num - 1:
#     print(num + 1, end = ' ')


# n = int(input())

# if n == 0:
#     print(0)

# for i in range(n):
#     for j in range(n):
#         value = min(i, j, n - i - 1, n - j - 1) + 1
#         print(value, end = ' ')
#     print()


# for i in range(n):
#     for j in range(n):
#         if i == num or j == num or i == n - num -1 or j == n- num - 1:
#             print(num + 1, end = ' ')
#         else: 
#             print(n // 2 + 1,end = ' ')
#     print()


n = int(input())
k = int(input())

for i in range(1, n + 1): 
    for j in range(1, n + 1):
        print(f'{i * j:^{k}}',end='')
        if j < n:
            print('|',end='')
    print('\n',"-" * (k*n + n-1), sep = '')