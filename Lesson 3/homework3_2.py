''' 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.'''
def personal_data(name = input("Введите свое имя: "), surname = input("Введите свою фамилию: "), year = input("Введите год рождения: "),
    city = input("Введите город проживания "),e_mail = input("Введите адрес электронной почты: "),ph_num = input("Введите номер своего телефона: ")):
    return(f"Имя - {name}; Фамилия- {surname}; год рождения - {year}; город проживания - {city}; email - {e_mail}; телефон - {ph_num}")
print(personal_data())