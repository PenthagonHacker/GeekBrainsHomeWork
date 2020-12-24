string = input('Введите несколько слов, разделённых пробеламии: ').split()

for word in string:
    if len(word) < 10:
        print(word)
    else:
        print(word[:10])

    