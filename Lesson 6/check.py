# def is_good(words):
#     letters = 'АБВ'
#     for word in words:
#         print(word[0].upper())
#         if not (word[0].upper() in letters):
#             return False

#     return True


# n = int(input())
# words = []

# for i in range(n):
#     words.append(input())

# if is_good(words):
#     print("YES")
# else:
#     print("NO")


# def cutter(to_cut, n):
#     if len(to_cut) > n:
#         return to_cut[:(n - 3)] + '...'
#     return to_cut


# size = int(input())

# n = int(input())

# for i in range(n):
#     print(cutter(input(), size))


# list <- num
# 7 2 3 * -
# list <- 7, list <- 2, list <- 3
# *
# list -> 3, list -> 2, list <- 3 * 2
# *
# list -> 3 * 2, list -> 7, list <- 7 - 3 * 2

# FIFO - First in First out
# Queue 

# LIFO - Last in First out
# Stack


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

ops = {
    '+': add,
    '-': sub,
    '*': mul,
}



def opn(oper):
    var = []

    for i in oper:
        if i.isdigit():
            var.append(int(i))
        else:
            tmp2 = var.pop()
            tmp1 = var.pop()
            var.append(ops[i](tmp1, tmp2))
    return var.pop()


operation = input().split()
print(opn(operation))
