#list
a = int(input("Введите номер месяца от 1 до 12: "))
year = ['', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if year.index(a) == 1 or year.index(a) == 2 or year.index(a) == 12:
	print("Выбранный Вами месяц соответствует сезону - Зима")
elif 2 < year.index(a) <= 5:
	print("Выбранный Вами месяц соответствует сезону - Весна")
elif 5 < year.index(a) <= 8:
	print("Выбранный Вами месяц соответствует сезону - Лето")
elif 8 < year.index(a) <= 11:
	print("Выбранный Вами месяц соответствует сезону - Осень")

#list
a = int(input("Введите номер месяца от 1 до 12: "))
seasons_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето",
		7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}
print("Выбранный Вами месяц соответствует сезону - " + seasons_dict.get(a))