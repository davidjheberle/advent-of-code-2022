import re
from collections import deque
from math import prod


def parse_input(input_file):
    items = []
    operations = []
    tests = []

    with open(input_file) as file:
        lines = deque([line.strip() for line in file])

    while lines:
        line = lines.popleft()
        data = re.split(r':\s*', line)
        cmd = data[0]
        if cmd == 'Starting items':
            items.append(deque(map(int, re.split(r',\s*', data[1]))))
        elif cmd == 'Operation':
            operations.append(re.split(r'\s*=\s*', data[1])[-1])
        elif cmd == 'Test':
            m = int(data[-1].split()[-1])
            t = int(lines.popleft().split()[-1])
            f = int(lines.popleft().split()[-1])
            tests.append([m, t, f])

    return items, operations, tests


def execute_operation(i, operation):
    x, op, y = operation.split()
    x = i if x == 'old' else int(x)
    y = i if y == 'old' else int(y)
    if op == '+':
        return x + y
    elif op == '*':
        return x * y


def execute_test(i, test):
    m, t, f = test
    return t if i % m == 0 else f


def run_part_1(input_file, rounds):
    items, operations, tests = parse_input(input_file)
    inspections = [0] * len(tests)

    for r in range(rounds):
        for m in range(len(tests)):
            while items[m]:
                inspections[m] += 1
                item = items[m].popleft()
                item = execute_operation(item, operations[m])
                item = item // 3
                destination = execute_test(item, tests[m])
                items[destination].append(item)

    max1 = max(inspections)
    inspections.remove(max1)
    max2 = max(inspections)
    print(max1 * max2)


def run_part_2(input_file, rounds):
    items, operations, tests = parse_input(input_file)
    inspections = [0] * len(tests)
    mod = prod(t[0] for t in tests)

    for r in range(rounds):
        for m in range(len(tests)):
            while items[m]:
                inspections[m] += 1
                item = items[m].popleft()
                item = execute_operation(item, operations[m])
                item = item % mod
                destination = execute_test(item, tests[m])
                items[destination].append(item)

    max1 = max(inspections)
    inspections.remove(max1)
    max2 = max(inspections)
    print(max1 * max2)


if __name__ == '__main__':
    run_part_1("./input.txt", 20)
    run_part_2("./input.txt", 10000)
