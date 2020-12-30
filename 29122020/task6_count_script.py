from itertools import count, islice
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Count script')
    parser.add_argument('start', type=int, help='Select the beginning of a list sequence')
    parser.add_argument('stop', type=int, help='Select the end of a list sequence')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    lst = islice(count(namespace.start), namespace.stop)

    print(list(lst))
