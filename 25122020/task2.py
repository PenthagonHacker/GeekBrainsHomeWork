# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def requesting_info(name, lastname, birth_year, current_city, email, phone_number):
    return f'Данные о пользователе: ' \
           f'Имя: {name}, Фамилия:{lastname}, Год рождения:{birth_year}, Город проживания:{current_city}, email:{email}, Телефон:{phone_number}'


foo = requesting_info(lastname='Masalov', birth_year=1987, email='vladislavmasalov@...ru', name='Vladislav',
                      current_city='Saint-Petersburg', phone_number=911)

print(foo)
