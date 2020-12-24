revenue = int(input("Введите сумму выручки: "))
costs = int(input("Введите сумму издержек: "))
result = revenue - costs
profitability = format(result / revenue * 100, '.2f')
if costs > revenue:
	print(f"Фирма сработала с убытком. Финансовый результат составил {result} руб.")
	
elif costs == revenue:
	print("Фирма окупила издержки, но не принесла прибыли")
	
else:
	print(f"Прибыль фирмы составила {result} руб.")
	print(f"Рентабельность выручки составила {profitability} процентов")
	unit = int(input("Введите количетво сотрудников фирмы: "))
	pofit_per_unit = format(result/ unit, '.1f')
	print(f"Прибыль на одного сотрудника оставила: {pofit_per_unit} руб.")