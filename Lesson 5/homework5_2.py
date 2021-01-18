"""2. Создать текстовый файл (не программно), 
сохранить в нем несколько строк, выполнить 
подсчет количества строк, количества слов в каждой строке."""
with open("out_file.txt") as out_f:
    lines = 0
    words = 0
    for line in out_f:
        lines += line.count("\n")
        words = line.split()
        print(f"Количество слов в строке {lines} - {len(words)}.")
    print(f"Количество строк в файле - {lines}")