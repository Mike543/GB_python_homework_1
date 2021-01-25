"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую 
построчно данные. При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл."""
dic = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('dictionary.txt', 'r') as dic_start:
    
    for i in dic_start:
        i = i.split(' ', 1)
        new_file.append(dic[i[0]] + '  ' + i[1])


with open('dictionary_2.txt', 'w') as dic_fin:
    dic_fin.writelines(new_file)
with open('dictionary_2.txt') as dic_fin:
    print(dic_fin.read())