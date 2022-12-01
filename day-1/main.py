def print_max(input_file):
    index = 0
    calories = 0
    max_calories = 0
    max_elf = 0

    with open(input_file) as file:
        for line in file:
            if line == '\n':
                if calories > max_calories:
                    max_calories = calories
                    max_elf = index
                calories = 0
                index += 1
            else:
                calories += int(line)

    print(max_elf, max_calories)


def print_max_x(input_file, count):
    index = 0
    calories = 0
    data = {}

    with open(input_file) as file:
        for line in file:
            if line == '\n':
                data[index] = calories
                calories = 0
                index += 1
            else:
                calories += int(line)

    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

    result = 0
    for i in range(count):
        result += sorted_data[i][1]

    print(sorted_data)
    print(result)


if __name__ == '__main__':
    print_max("./input.txt")
    print_max_x("./input.txt", 3)
