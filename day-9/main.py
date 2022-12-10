def normalize(i):
    if i > 0:
        return 1
    elif i < 0:
        return -1
    return 0


def parse_direction(point, direction):
    if direction == 'U':
        position = point[0], point[1] - 1
    elif direction == 'D':
        position = point[0], point[1] + 1
    elif direction == 'L':
        position = point[0] - 1, point[1]
    elif direction == 'R':
        position = point[0] + 1, point[1]
    return position


def move_knot(rope, index, position):
    if index == len(rope)-1:
        rope[index] = position
    else:
        this_knot = rope[index] = position
        next_knot = rope[index+1]
        diff = this_knot[0] - next_knot[0], this_knot[1] - next_knot[1]
        if abs(diff[0]) > 1 or abs(diff[1]) > 1:
            position = next_knot[0] + normalize(diff[0]), next_knot[1] + normalize(diff[1])
            move_knot(rope, index+1, position)


def parse_input(input_file, knots):
    start = 0, 0
    rope = []
    for i in range(knots):
        rope.append(start)
    unique = set()
    unique.add(start)

    with open(input_file) as file:
        for line in file:
            direction, amount = line.strip().split()
            amount = int(amount)
            for i in range(amount):
                position = parse_direction(rope[0], direction)
                move_knot(rope, 0, position)
                unique.add(rope[-1])

    return len(unique)


def run_part_1(input_file):
    print(parse_input(input_file, 2))


def run_part_2(input_file):
    print(parse_input(input_file, 10))


if __name__ == '__main__':
    run_part_1("./input.txt")
    run_part_2("./input.txt")
