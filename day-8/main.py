class Tree:

    def __init__(self, height, visible):
        self.height = height
        self.visible = visible
        self.scenic_right = 0
        self.scenic_left = 0
        self.scenic_up = 0
        self.scenic_down = 0

    def __str__(self):
        return 'height: ' + str(self.height) + ', visible: ' + str(self.visible)

    def get_scenic_score(self):
        return self.scenic_right * self.scenic_up * self.scenic_down * self.scenic_left


def run_part_1(input_file):
    count = 0
    forest = []

    with open(input_file) as file:
        i = 0
        for line in file:
            forest.append([])
            data = line.strip()
            for tree in data:
                forest[i].append(Tree(int(tree), False))
            i += 1

    len_i = len(forest)
    for i in range(len_i):
        len_j = len(forest[i])
        for j in range(len_j):
            tree = forest[i][j]

            if tree.visible is False:
                tree.visible = (i == 0 or i == len_i-1 or j == 0 or j == len_j-1)

            if tree.visible is False:
                # look left
                for k in range(j-1, -1, -1):
                    other = forest[i][k]
                    if tree.height > other.height:
                        if k == 0:
                            tree.visible = True
                            break
                    else:
                        break

            if tree.visible is False:
                # look right
                for k in range(j+1, len_j, 1):
                    other = forest[i][k]
                    if tree.height > other.height:
                        if k == len_j-1:
                            tree.visible = True
                            break
                    else:
                        break

            if tree.visible is False:
                # look up
                for k in range(i-1, -1, -1):
                    other = forest[k][j]
                    if tree.height > other.height:
                        if k == 0:
                            tree.visible = True
                            break
                    else:
                        break

            if tree.visible is False:
                # look down
                for k in range(i+1, len_i, 1):
                    other = forest[k][j]
                    if tree.height > other.height:
                        if other.visible or k == len_i-1:
                            tree.visible = True
                            break
                    else:
                        break

            if tree.visible:
                count += 1

    print(count)


def run_part_2(input_file):
    best = 0
    forest = []

    with open(input_file) as file:
        i = 0
        for line in file:
            forest.append([])
            data = line.strip()
            for tree in data:
                forest[i].append(Tree(int(tree), False))
            i += 1

    len_i = len(forest)
    for i in range(len_i):
        len_j = len(forest[i])
        for j in range(len_j):
            tree = forest[i][j]

            # look left
            for k in range(j-1, -1, -1):
                other = forest[i][k]
                tree.scenic_left += 1
                if tree.height <= other.height:
                    break

            # look right
            for k in range(j+1, len_j, 1):
                other = forest[i][k]
                tree.scenic_right += 1
                if tree.height <= other.height:
                    break

            # look up
            for k in range(i-1, -1, -1):
                other = forest[k][j]
                tree.scenic_up += 1
                if tree.height <= other.height:
                    break

            # look down
            for k in range(i+1, len_i, 1):
                other = forest[k][j]
                tree.scenic_down += 1
                if tree.height <= other.height:
                    break

            score = tree.get_scenic_score()
            if score > best:
                best = score

    print(best)


if __name__ == '__main__':
    run_part_1("./input.txt")
    run_part_2("./input.txt")
