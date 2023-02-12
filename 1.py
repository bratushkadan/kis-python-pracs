from math import ceil


def main(x, y, z):
    numeratorA = 86 * ceil(y - 39) ** 2 - 54 * (x ** 3 - 0.04 - z) ** 5
    denominatorA = (x ** 3 + 47 * z) ** 3 / 52 - y / 97
    numeratorB = 90 * (z ** 2 + 27 * y ** 3 + 16 * x) ** 4
    denominatorB = 54 * (y + z ** 2) - (16 * x ** 2) ** 4 / 42
    return numeratorA / denominatorA - numeratorB / denominatorB
