# # Class
# # CapWord - каждое слово разделено заглавной буквой

# class Car(): 
#     # __init__() -> встроенная функция конструктор
#     def __init__(self, name:str, weight:int):
#         self.name = name
#         self.weight = weight
#         self.engine = False

#     def switch_engine(self):
#         self.engine = not self.engine

#     def hello(self, car):
#         return f'hello {self.name, car.name}'

    
# # Class Student(name, grade) -> take_grade()
# # Atributes: name, grade
# # Methods: take_grade(grade)
# # 1 example

# car1 = Car('Toyota', 12000)
# print(car1.name, car1.engine)
# car1.switch_engine()
# print(car1.name, car1.engine)
# print(car1.hello(car2))


# # int

# print(1.0, type(1.0))


# list_cars = []
# for i in range(10):
#     list_cars.append(Car(name=f'{i}', weight=i))






# class RedButton:
#     def __init__(self):
#         self._count = 0

#     def click(self):
#         self._count += 1
#         print('Тревога!')

#     def count(self):
#         return self._count
    
# a = RedButton()

# a.click(
# )
# a.click()

# print(a.count())



class Programmer:
    dict_earns = {
            'Junior': 10,
            'Middle': 15,
            'Senior': 20
    }

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.work_hours = 0
        self.earn_hour = self.dict_earns[self.grade]
        self.earn = 0

    def rise(self):
        if self.grade == 'Junior':
            self.grade = 'Middle'
            self.earn_hour = self.dict_earns[self.grade]
            return
        if self.grade == 'Middle':
            self.grade = 'Senior'
            self.earn_hour = self.dict_earns[self.grade]
            return
        if self.grade == 'Senior':
            self.earn_hour += 1
            return
    
    def work(self, hour):
        self.work_hours += hour
        print(self.earn_hour, hour)
        self.earn += self.earn_hour * hour

    def info(self):
        return f'{self.name} {self.work_hours}ч. {self.earn}тгр.'
    
programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())