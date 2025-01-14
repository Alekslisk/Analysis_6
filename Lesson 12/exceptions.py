# print(10 / 0)

# print(int('слово'))
# print(float('слово'))

a = (input())
b = (input())

# try: # Блок в котором может возникнуть ошибка
#     # file = open('a.txt')
#     a = int(a)
#     b = int(b)
#     print(a / b)
# # catch:
# # except: # Блок обработки ошибки
# #     print('Что то не так') 
# except ValueError:
#     print('Проблема с преврашением в int')
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')
# finally: # Блок который сработает в любом случае
#     # file.close()
#     print('Финально')

print('Да я работаю')

class MyOwnError(Exception):
    def __init__(self):
        super().__init__('Non acceptable value')
        
        # ZeroDivisionError     

def error_function(value):
    if value != 0:
        raise MyOwnError
    return value

try: # Блок в котором может возникнуть ошибка
    # file = open('a.txt')
    a = int(a)
    b = int(b)
    if b == 0:
        raise MyOwnError
    print(a / b)
# catch:
# except: # Блок обработки ошибки
#     print('Что то не так') 
except MyOwnError as e:
    print(e)
except ValueError:
    print('Проблема с преврашением в int')
except ZeroDivisionError:
    print('Нельзя делить на ноль')
finally: # Блок который сработает в любом случае
    # file.close()
    print('Финально')