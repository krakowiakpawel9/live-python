print(__name__)


def calc(a, b):
    return a * b, a + b, a - b


if __name__ == '__main__':
    print('if block running...')
    print(calc(2, 3))
