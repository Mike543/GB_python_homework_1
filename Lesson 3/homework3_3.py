'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.'''
def my_func(arg_1 = input("Укажите первое число: "), arg_2 = input("Укажите второе число "), arg_3 = input("Укажите третье число: ")):
    try:
    	return int(arg_1) + int(arg_2) + int(arg_3) - int(min(arg_1, arg_2, arg_3))
    except ValueError:
    	print('Введено не число!')
print(my_func())