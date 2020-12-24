my_list = [7, 5, 3, 3, 2]
my_list.append(int(input('Введите натуральное целое число: ')))
new_list = sorted(my_list)
new_list.reverse()
print(new_list)