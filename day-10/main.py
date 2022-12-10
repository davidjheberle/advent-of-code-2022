from collections import deque


def execute(stack, instructions):
    if stack:
        return stack.popleft()
    instruction = instructions.popleft().strip().split()
    op = instruction[0]
    if op == 'addx':
        stack.append(int(instruction[1]))
    return 0


def render(cursor, x):
    if abs(x - cursor % 40) < 2:
        return '#'
    return '.'


def run_part_1(input_file, start, stop, step):
    x = 1
    stack = deque([])
    instructions = deque([])
    cycle = 0
    signals = []
    cycles = list(range(start, stop + 1, step))

    with open(input_file) as file:
        instructions.extend(file.readlines())

    while instructions:
        cycle += 1
        if cycle in cycles:
            signals.append(cycle * x)
        x += execute(stack, instructions)

    print(sum(signals))


def run_part_2(input_file):
    x = 1
    stack = deque([])
    instructions = deque([])
    cursor = 0
    screen = ''

    with open(input_file) as file:
        instructions.extend(file.readlines())

    while instructions:
        screen += render(cursor, x)
        x += execute(stack, instructions)
        cursor += 1
        if cursor % 40 == 0:
            screen += '\n'

    print(screen)


if __name__ == '__main__':
    run_part_1("./input.txt", 20, 220, 40)
    run_part_2("./input.txt")
