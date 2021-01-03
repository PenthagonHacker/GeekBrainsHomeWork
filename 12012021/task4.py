import os


translate = [('One', 'Один'), ('Two', 'Два'), ('Three', 'Три'), ('Four', 'Четыре')]
with open('task4.txt', encoding='utf-8') as task4:
    with open('task4_translated.txt', 'x', encoding='windows-1251') as task4_new:
        for line in task4.readlines():
            for en, rus in translate:
                if en in line:
                    new_line = line.replace(en, rus)
                    task4_new.write(new_line)
print(f"Файл был успешно записан. Вы можете найти его по адресу {os.path.join(os.getcwd(), 'task4_new.txt')}")