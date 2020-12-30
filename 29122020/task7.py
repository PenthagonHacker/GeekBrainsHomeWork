def fact(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
        yield result


for el in fact(5):
    print(el, end=' ')
