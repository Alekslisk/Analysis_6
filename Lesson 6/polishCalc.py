# binary
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a // b


# unary
def chainge(a):
    return -1 * a


def fact(a):
    tmp = 1
    while a > 1:
        tmp *= a
        a -= 1
    return tmp

def clone(a):
    return (a,a)


#ternary 
def ter_chainge(a ,b , c):
    return(b, c, a)

ops = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '~': chainge,
    '!': fact,
    '#': clone,
    '@': ter_chainge,
}

def opn(oper):
    var = []

    for i in oper:
        if i.isdigit():
            var.append(int(i))
        elif i in '@':
            tmp3 = var.pop()
            tmp2 = var.pop()
            tmp1 = var.pop()
            for i in [*ops[i](tmp1, tmp2, tmp3)]:
                var.append(i)
        elif i in '~!':
            tmp1 = var.pop()
            var.append(ops[i](tmp1))
        elif i in '#':
            tmp1 = var.pop()
            for i in [*ops[i](tmp1)]:
                var.append(i)
        else:
            tmp2 = var.pop()
            tmp1 = var.pop()
            var.append(ops[i](tmp1, tmp2))
    return var.pop()


operation = input().split()
print(opn(operation))
