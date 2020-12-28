my_list = []
my_list.append(input('Введите первое значение списка: '))
my_list.append(input('Введите второе значение списка: '))
my_list.append(input('Введите третье значение списка: '))
my_list.append(input('Введите четвертое значение списка: '))
my_list.append(input('Введите пятое значение списка: '))
my_list.insert(0, my_list.pop(1))
my_list.insert(2, my_list.pop(3))
print(my_list)