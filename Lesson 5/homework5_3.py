"""3. Создать текстовый файл (не программно), 
построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников."""
with open("salary.txt") as my_file:

	salary_sum = 0 
	salary_num = 0

	for line in my_file:
		name, salary = line.split()
		salary = int(salary)
		salary_sum += salary
		salary_num += 1
		if salary < 20000:
			print(name)

print("Средняя зарплата = ", salary_sum / salary_num)