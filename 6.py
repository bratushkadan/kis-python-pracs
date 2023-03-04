def main(a):
    tree = {
        (1989, 'YAML'): 9,
        (1989, 'SCSS'): 10,
        (1969, 'YAML', 'MQL5'): 4,
        (1969, 'YAML', 'BLADE', 1978): 2,
        (1969, 'YAML', 'BLADE', 2009): 3,
        (1969, 'YAML', 'CLICK', 1978): 0,
        (1969, 'YAML', 'CLICK', 2009): 1,
        (1969, 'SCSS', 'SQL'): 5,
        (1969, 'SCSS', 'SLASH'): 6,
        (1969, 'SCSS', 'EJS', 1978): 7,
        (1969, 'SCSS', 'EJS', 2009): 8
    }

    for t, v in tree.items():
        s1 = set(t)
        s2 = set(a)

        if len((s1 & s2)) == len(s1):
            return v
