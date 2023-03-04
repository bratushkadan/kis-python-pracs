field_num = [0, 10, 12, 13, 16, 20]


def main(y):
    r = 0
    for count, key in enumerate(y):
        v = int(y[key])
        s = v << field_num[count]
        r |= s
    return r
