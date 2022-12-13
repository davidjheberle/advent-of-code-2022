from collections import deque


def parse_input(input_file, start):
    with open(input_file) as file:
        height_map = {
            (x, y): s
            for x, row in enumerate(file.read().splitlines())
            for y, s in enumerate(row)
        }

    starts = {k for k, v in height_map.items() if v == start}
    end = next(k for k, v in height_map.items() if v == 'E')

    for start in starts:
        height_map[start] = 'a'
    height_map[end] = 'z'

    return height_map, starts, end


def adjacent(x, y):
    return (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)


def find_shortest_path(input_file, start):
    height_map, starts, end = parse_input(input_file, start)

    distance = {}
    bfs = deque([(0, x) for x in starts])

    while len(bfs) > 0:
        t, p = bfs.popleft()
        if p in distance:
            continue
        distance[p] = t

        for q in adjacent(*p):
            if ord(height_map.get(q, '~')) - ord(height_map[p]) > 1:
                continue
            bfs.append((t + 1, q))

    print(distance[end])


def run_part_1(input_file):
    find_shortest_path(input_file, 'S')


def run_part_2(input_file):
    find_shortest_path(input_file, 'a')


if __name__ == '__main__':
    run_part_1("./input.txt")
    run_part_2("./input.txt")
