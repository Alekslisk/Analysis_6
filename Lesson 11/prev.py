class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f'Name: {self.name}'
    
    def talk(self):
        return 'BlaBlaBla'
    
# OOP:
# 1. Инкапсулация
# 2. Полиморфизм
# 3. Наследование


person1 = Person('Alex', 21)

print('Hello' + person1.info())

print(person1.talk())

# 1. Инкапсулация


# __ перед атрибутов делают его private 
class Phone:
    def __init__(self, model, price):
        self.__model = model
        self.__price = price

    # Getter -> берет информацию из класса
    def GetPrice(self):
        return self.__price

    # Setter -> названчает информацию в класс
    def SetPrice(self, price):
        if price < 0:
            raise TypeError
        self.__price = price
    


phone1 = Phone('M', 1200)

# print(phone1.GetPrice())
    

# phone1.__price =  -1000

# print(phone1.GetPrice())

# phone1.SetPrice(10)

# print(phone1.GetPrice())

# phone1.SetPrice(-10)

# print(phone1.GetPrice())

# Наследование

# Родительский класс (Base class)
class Animal:
    def __init__(self, name: str, weight: int, flag_carnivorous: bool):
        self.__name = name
        self.__weight = weight
        self.__flag_carnivorous = flag_carnivorous
    
    def eat(self):
        return 'NomNom'
    
    def dish(self):
        if self.__flag_carnivorous:
            return 'meat'
        return 'grass'

    def voice(self):
        return ''
    
    def __str__(self) -> str:
        animal_type = 'predator' if self.__flag_carnivorous else 'non predator'
        return f'Name: {self.__name} Weight: {self.__weight} Type: {animal_type}'

# Дочерний класс (Child class)
class Cat(Animal):
    def voice(self):
        return 'Meow'

# Дочерний класс (Child class)
class Goat(Animal):
    def voice(self):
        return 'Beee'



cat1 = Cat('Barsik', 5, True)
print(cat1.voice())
print(cat1.dish())

goat1 = Goat('Bob', 12, False)
print(goat1.voice())
print(goat1.dish())

print(type(goat1).mro())


# Полморфизм
# Одинаковое название метода , НО разнаяр реализация
print('Часть по полиморфизм')
class_list = [goat1, cat1, phone1]

for i in class_list:
    if issubclass(type(i), Animal):
        print(i.voice())
        print(i.dish())
        print(i)


# Magic methods 

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.normalize_time()
    
    def normalize_time(self): # 200 // 60 == 3, 200 % 60 = 20
        self.__minutes += self.__seconds // 60
        self.__seconds %= 60
        self.__hours += self.__minutes // 60
        self.__minutes %= 60
        self.__hours %= 24

    def __str__(self):
        return f'{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}'
    
    def __add__(self, other):
        if isinstance(other, Time):
            return Time(
                self.__hours + other.getHours(),
                self.__minutes + other.getMinutes(),
                self.__seconds + other.getSeconds(),
            )
        return  TypeError('Можно складывать только обекты Time')
    
    def __sub__(self, other):
        if isinstance(other, Time):
            return Time(
                self.__hours - other.getHours(),
                self.__minutes - other.getMinutes(),
                self.__seconds - other.getSeconds(),
            )
        return  TypeError('Можно отнимать только обекты Time')
    
    def __eq__(self, other):
        if isinstance(other, Time):
            return (self.__hours, self.__minutes, self.__seconds) == (other.getHours(), other.getMinutes(), other.getSeconds())
        return  TypeError('Можно сравнивать только обекты Time')

    def __lt__(self, other): # <
        if isinstance(other, Time):
            return (self.__hours, self.__minutes, self.__seconds) < (other.getHours(), other.getMinutes(), other.getSeconds())
        return  TypeError('Можно сравнивать только обекты Time')

    def __le__(self, other): # <=
        if isinstance(other, Time):
            return self == other or self < other
        return  TypeError('Можно сравнивать только обекты Time')
       

    def getHours(self):
        return self.__hours
    
    def getMinutes(self):
        return self.__minutes
    
    def getSeconds(self):
        return self.__seconds
    

time1 = Time(12,0,0)

time2 = Time(15,0,200)
# __str__
print(time1, time2)

# __add__
print(time1 + time2)

# __sub__
print(time1 - time2)

# __eq__
print(time1 == time2)

# __sub__
print(time1 < time2)

# __eq__
print(time1 <= time2)

# __eq__
print(time1 - 5)











# Практическое задание

# Vector, Point

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(
                self.x + other.x,
                self.y + other.y
            )

    def __str__(self):
        return f'({self.x}, {self.y})'
    
class Vector:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(
                self.start + other.start,
                self.end + other.end
            )