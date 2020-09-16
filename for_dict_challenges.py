# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
list1 = [i.get('first_name') for i in students]
for i in list(set(list1)):
    print(f'{i}: {list1.count(i)} ')
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

list1 = [i.get('first_name') for i in students]
dict1 = [list1.count(i) for i in list(set(list1))]
print(f'Самое частое имя: {list(set(list1))[dict1.index(max(dict1))]}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
]
for k, i in enumerate(school_students, 1):
    names = [j.get('first_name') for j in i]
    c_names = [names.count(j) for j in list(set(names))]
    print(f'Самое частое имя в классе {k}: {list(set(names))[c_names.index(max(c_names))]}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

for i in school:
    male = 0
    female = 0
    for k in [j.get('first_name') for j in i['students']]:
        if is_male[k] == True:
            male += 1
        else:
            female += 1
    print(f'В классе {i["class"]} {male} мальчиков и {female} девочек')

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

l_male=[]
l_female=[]
l_class=[]
for i in school:
    male = 0
    female = 0
    for k in [j.get('first_name') for j in i['students']]:
        if is_male[k] == True:
            male += 1
        else:
            female += 1
    l_class.append(i["class"])
    l_male.append(male)
    l_female.append(female)
print(f'Больше всего мальчиков в классе {l_class[l_male.index(max(l_male))]}')
print(f'Больше всего мальчиков в классе {l_class[l_female.index(max(l_female))]}')


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
