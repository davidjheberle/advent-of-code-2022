def run_part_1(input_file):
    stacks = [[], [], [], [], [], [], [], [], []]
    phase = 0

    with open(input_file) as file:
        for line in file:
            if phase == 0:
                if line[1] == '1':
                    phase = 1
                    for stack in stacks:
                        stack.reverse()
                    continue
                for stack_index in range(9):
                    index = 1 + stack_index * 4
                    box = line[index]
                    if box != ' ':
                        stacks[stack_index].append(box)
            else:
                instructions = line.strip()
                if instructions == '':
                    continue
                _, n, _, s, _, d = instructions.split()
                n = int(n)
                s = int(s)-1
                d = int(d)-1
                for _ in range(n):
                    box = stacks[s].pop()
                    stacks[d].append(box)

    for stack in stacks:
        print(stack[-1], end='')
    print()


def run_part_2(input_file):
    stacks = [[], [], [], [], [], [], [], [], []]
    phase = 0

    with open(input_file) as file:
        for line in file:
            if phase == 0:
                if line[1] == '1':
                    phase = 1
                    for stack in stacks:
                        stack.reverse()
                    continue
                for stack_index in range(9):
                    index = 1 + stack_index * 4
                    box = line[index]
                    if box != ' ':
                        stacks[stack_index].append(box)
            else:
                instructions = line.strip()
                if instructions == '':
                    continue
                _, n, _, s, _, d = instructions.split()
                n = int(n)
                s = int(s)-1
                d = int(d)-1
                boxes = []
                for _ in range(n):
                    boxes.append(stacks[s].pop())
                for _ in range(len(boxes)):
                    stacks[d].append(boxes.pop())

    for stack in stacks:
        print(stack[-1], end='')
    print()


if __name__ == '__main__':
    run_part_1("./input.txt")
    run_part_2("./input.txt")
