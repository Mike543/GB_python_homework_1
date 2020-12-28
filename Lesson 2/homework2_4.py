my_str = input("Введите пять слов разделенных пробелами: ")
my_string = my_str.split()
my_list = []
my_list.append((my_string[0])[0:10])
my_list.append((my_string[1])[0:10])
my_list.append((my_string[2])[0:10])
my_list.append((my_string[3])[0:10])
my_list.append((my_string[4])[0:10])
for ind, el in enumerate(my_list):
    print(ind, el)