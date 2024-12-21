def create_car(name, weight):
    return {
        'name' : name,
        'weight':weight,
        'flag_engine': False
    }

def engine_on(car):
    car['flag_engine'] = True

car_1 = create_car('Toyota', 12)

print(car_1)

engine_on(car_1)

print(car_1)
