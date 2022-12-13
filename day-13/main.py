from math import prod


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    if isinstance(left, list) and isinstance(right, list):
        for lhs, rhs in zip(left, right):
            if result := compare(lhs, rhs):
                return result
        return len(left) - len(right)

    if isinstance(left, int):
        return compare([left], right)

    if isinstance(right, int):
        return compare(left, [right])

    assert False


class Comparator:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return compare(self.x, other.x) < 0

    def __eq__(self, other):
        return compare(self.x, other.x) == 0


def run_part_1(input_file):
    with open(input_file) as file:
        pairs = [[eval(x) for x in pair.splitlines()] for pair in file.read().split("\n\n")]
    print(sum(i + 1 for i, (left, right) in enumerate(pairs) if compare(left, right) < 0))


def run_part_2(input_file):
    with open(input_file) as file:
        packets = [eval(x) for x in file.read().splitlines() if len(x) > 0]
    dividers = [[2]], [[6]]
    result = sorted([*packets, *dividers], key=Comparator)
    print(prod(result.index(x) + 1 for x in dividers))


if __name__ == '__main__':
    run_part_1("./input.txt")
    run_part_2("./input.txt")
