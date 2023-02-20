def main(n):
    if n == 0:
        return -.28
    if n >= 1:
        return main(n - 1) + 14 * main(n - 1) ** 6
