import re


# email = 'kldjflksdjflksjd@gmail.com kldjflksdjflksjd'

# #Search первое совпадение

# # match проверяет с начала строки
# match = re.match(r'$@gmail.com', email)

# help(re)

# print(match)

# phone = '+-123-456-7890'

# if re.fullmatch(r'\+\d{1,3}-\d{3}-\d{3}-\d{4}', phone):
#     print('Yes')
# else:
#     print('No')


phone_1 = '+A4-(123)-456-7890'
phone_2 = '+1 (123) 456 7890'
phone_3 = '234 456-7890'

re_phone = r'(\+\D{1}\d{1}[- ])(\(\d{3}\)|\d{3})[- ]\d{3}[- ]\d{4}'

if re.fullmatch(re_phone, phone_1):
    print('Yes')
else:
    print('No')

if re.fullmatch(re_phone, phone_2):
    print('Yes')
else:
    print('No')

if re.fullmatch(re_phone, phone_3):
    print('Yes')
else:
    print('No')

text = 'Привет , hello Almаty это Good'

pattern = r'[А-Яа-яЁё]'

matches = re.findall(pattern, text)

print(matches)

cyrilic_to_latin = {'а':'а', 'П':'P', 'ш': 'sh'}

def replace_cyrilic(match):
    return cyrilic_to_latin.get(match.group(0), match.group(0))

result = re.sub(pattern, replace_cyrilic, text)

print(result)