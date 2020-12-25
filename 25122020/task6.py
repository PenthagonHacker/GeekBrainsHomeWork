def int_func(text: str):
    new_text = ' '.join(map(lambda x: x.title(), text.split()))
    return new_text






print(int_func('some random text'))
print(int_func('somerandomtext'))
