# find

# to_find = 9
# list_find = [1,2,3,4,5,6,10,10,213,324,435,122,3354,23,213,4325,323,1]

# flag_find = False

# for i in list_find:
#     if i == to_find:
#         flag_find = True
#         break

# print(flag_find) 

# binary find
import random
list_find_bin = []

for i in range(100):
    list_find_bin.append(random.randrange(0,10000))
list_find_bin.sort()
print(list_find_bin)

to_find_bin = list_find_bin[len(list_find_bin) - 1]

left = 0

right = len(list_find_bin) - 1



flag_find = False
cnt = 0
for i in list_find_bin:
    cnt += 1
    if i == to_find_bin:
        flag_find = True
        break


flag_find_bin = False
cnt_bin = 0
while left <= right:
    cnt_bin += 1
    mid = (left + right) // 2

    if list_find_bin[mid] == to_find_bin:
        flag_find_bin = True
        break
    elif list_find_bin[mid] < to_find_bin:
        left = mid + 1
    else:
        right = mid - 1
print(cnt_bin)

print(flag_find_bin)

print(cnt)


print(list_find_bin.index(-1))