def main(a, b, n, x):
    s1 = sum([(4 * (1 - j ** 2 - j / 64) ** 4 + j ** 5)
             for j in range(1, a + 1)])

    s2 = 0
    for j in range(1, n + 1):
        p = 1
        for i in range(1, a + 1):
            s3 = 0
            for c in range(1, b + 1):
                s3 += 28 * (72 - j ** 2 - 3 * c) ** 2 - \
                    (1 - x ** 3) ** .5 / 23 - 16 * i ** 5
            p *= s3
        s2 += p

    return s1 + s2
