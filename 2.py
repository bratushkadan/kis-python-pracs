def main(x):
    if x < 99:
        return x ** 9
    if x < 178:
        return 26 * abs(x) ** 6
    if x < 277:
        return x ** 4 - 44 * x ** 3
    if x < 312:
        return x ** 6
    return (51 * x + 66 + x ** 3) ** 4 + 24 * (x / 35 + 1) ** 5
