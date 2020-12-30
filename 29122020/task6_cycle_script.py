from itertools import islice, cycle
import argparse


string = input('Enter a string for the test purposes: ').split()


def create_parser():
    parser = argparse.ArgumentParser(description='Cycle script')
    parser.add_argument('stop', type=int, help='Select how many iterations you want to proceed')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    endless_string = list(islice(cycle(string), namespace.stop))

    print(endless_string)
