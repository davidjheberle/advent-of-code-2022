import json


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return None if left == right else left < right
    elif isinstance(left, int):
        left = [left]
    elif isinstance(right, int):
        right = [right]

    for lhs, rhs in zip(left, right):
        result = compare(lhs, rhs)
        if result is not None:
            return result

    return len(left) <= len(right)


def run_part_1(input_file):
    correct = []
    with open(input_file) as file:
        lines = []
        for line in file.readlines():
            line = line.strip()
            if line:
                lines.append(line)

    for i in range(0, len(lines), 2):
        left = json.loads(lines[i])
        right = json.loads(lines[i+1])

        if compare(left, right):
            correct.append(i//2+1)

    print(correct)
    print(sum(correct))


if __name__ == '__main__':
    run_part_1("./input.txt")
