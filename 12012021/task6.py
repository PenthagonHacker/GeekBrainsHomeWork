with open('task6.txt', encoding='utf-8') as task6:
    lectures_dict = {}
    for line in task6.readlines():
        new_line = line.replace('-', '')
        lectures_dict.update({new_line.split()[0]: sum(map(int, new_line.split()[1:]))})
print(lectures_dict)
