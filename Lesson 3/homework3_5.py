'''5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
 При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
 разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
  Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.'''
def my_sum ():
    common_sum = 0
    exit = False
    while exit == False:
        number = input('Input numbers or Q for quit - ').split()
        current_sum = 0
        for el in number:
            if el == 'q' or el == 'Q':
                number.remove(el)
                exit = True
                break
            else:
                try:
                    current_sum += int(el)
                except ValueError:
                    number.remove(el)
                    continue
            common_sum += current_sum
        print(f'Общая сумма чисел = {common_sum}')
my_sum()
