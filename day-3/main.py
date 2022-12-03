priority = '.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def run_part_1(input_file):
    total = 0

    with open(input_file) as file:
        for line in file:
            sack = line.strip()
            length = len(sack)
            compartment_1 = set(sack[:length//2])
            compartment_2 = set(sack[length//2:])
            errors = compartment_1 & compartment_2

            for error in errors:
                total += priority.index(error)

    print(total)


def run_part_2(input_file):
    total = 0
    index = 0
    sacks = []

    with open(input_file) as file:
        for line in file:
            sack = set(line.strip())
            sacks.append(sack)

            if index == 2:
                badges = sacks[0] & sacks[1] & sacks[2]
                for badge in badges:
                    total += priority.index(badge)
                index = 0
                sacks.clear()
            else:
                index += 1

    print(total)


if __name__ == '__main__':
    run_part_1("./input.txt")
    run_part_2("./input.txt")
