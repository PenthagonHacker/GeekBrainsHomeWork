with open('task6.txt', encoding='utf-8') as task6:
    lectures_dict = {}
    lst = ['-', '(л)', '(пр)', '(лаб)']
    for new_line in task6.readlines():
        for item in lst:
            if item in new_line:
                new_line = new_line.replace(item, '')
        lectures_dict.update({new_line.split()[0]: sum(map(int, new_line.split()[1:]))})
print(lectures_dict)


