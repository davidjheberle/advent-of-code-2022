def parse_line(line):
    p = line.strip()
    a, b = p.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')
    return int(a1), int(a2), int(b1), int(b2)


def run_part_1(input_file):
    count = 0

    with open(input_file) as file:
        for line in file:
            a1, a2, b1, b2 = parse_line(line)
            if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
                count += 1

    print(count)


def run_part_2(input_file):
    count = 0

    with open(input_file) as file:
        for line in file:
            a1, a2, b1, b2 = parse_line(line)
            ra = range(a1, a2+1)
            rb = range(b1, b2+1)
            if a1 in rb or a2 in rb or b1 in ra or b2 in ra:
                count += 1

    print(count)


if __name__ == '__main__':
    run_part_1("./input.txt")
    run_part_2("./input.txt")
