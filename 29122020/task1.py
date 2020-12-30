import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Employee salary calculation')
    parser.add_argument('-r', action='store', dest='rate', type=int, required=True, help='Wage per hour')
    parser.add_argument('-t', action='store', dest='hours', type=int, required=True,
                        help='Amount of working hours of a certain employee')
    parser.add_argument('-b', action='store', dest='bonus', type=int, required=True,
                        help='Input a bonus that is meant for Employee')
    return parser


if __name__ == '__main__':
    def calculate_salary():
        parser = create_parser()
        namespace = parser.parse_args()
        return f'Employee salary is {namespace.rate * namespace.hours + namespace.bonus}'


    p = calculate_salary()

    print(p)

#Для информации по скрипту требуется ввести task1.py --help