# def recursive_digit_sum(num):
#     if num < 10:
#         return num
#     return recursive_digit_sum(num // 10) + recursive_digit_sum(num % 10)

# result = recursive_digit_sum(7321346)

# print(result)

# def answer(f):

#     def dec_f(*args, **kwargs):
#         return f'Результат функции: {f(*args, **kwargs)}'
        
#     return dec_f

# @answer
# def a_plus_b(a, b):
#     return a + b


# print(a_plus_b(3, 5))
# print(a_plus_b(7, 9))



# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2

#         left_half = nums[:mid]
#         right_half = nums[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 nums[k] = left_half[i]
#                 i += 1
#             else:
#                 nums[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             nums[k] = left_half[i]
#             i += 1
# #             k += 1

# #         while j < len(right_half):
# #             nums[k] = right_half[j]
# #             j += 1
# #             k += 1


# # arr = [3, 2, 1, 5, 2, 3]
# # print(arr)
# # merge_sort(arr)
# # print(arr)
        
            

# def merge(arr1, arr2):
#     result = []
#     i = j = 0

#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             result.append(arr1[i])
#             i += 1
#         else:
#             result.append(arr2[j])
#             j += 1

#     while i < len(arr1):
#         result.append(arr1[i])
#         i += 1
#     while j < len(arr2):
#         result.append(arr2[j])
#         j += 1

#     return result

    

# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
    
#     mid = len(nums) // 2

#     left_arr = merge_sort(nums[:mid])
#     right_arr = merge_sort(nums[mid:])

#     return merge(left_arr, right_arr)
    

# print(merge_sort([3, 2, 1, 5, 2, 3]))       
            
# def fibonacci(n):
#     n_1, n_2 = 0, 1
#     for i in range(n + 1):
#         yield n_1
#         n_1, n_2 = n_2, n_1 + n_2

# print(*fibonacci(5))

def make_linear(arr):
    if not arr:
        return []

    if isinstance(arr[0], list):
        return make_linear(arr[0]) + make_linear(arr[1:])
    return [arr[0]] + make_linear(arr[1:])

print(make_linear([1, 2, [3]]))