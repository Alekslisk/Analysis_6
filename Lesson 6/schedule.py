def schedule(days):
    sequence = ['Манная', 'Гречневая', 'Пшённая',
    'Овсяная',
    'Рисовая'
    ]
    schedule_breakfast = []
    for i in range(days):
        schedule_breakfast.append(sequence[i % 5])


def print_schedule(days):
    for i in schedule(days):
        print(i)


days = int(input())
print_schedule(days)