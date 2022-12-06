def find_marker(input_file, distinct):
    count = 0
    marker = ""

    with open(input_file) as file:
        for line in file:
            data = line.strip()
            for letter in data:
                if letter in marker:
                    marker = marker[marker.index(letter) + 1:]
                marker += letter
                count += 1
                if len(marker) == distinct:
                    break

    return count


def run_part_1(input_file):
    print(find_marker(input_file, 4))


def run_part_2(input_file):
    print(find_marker(input_file, 14))


if __name__ == '__main__':
    run_part_1("./input.txt")
    run_part_2("./input.txt")
