class Tree:

    def __init__(self, height, visible):
        self.height = height
        self.visible = visible

    def __str__(self):
        return 'height: ' + str(self.height) + ', visible: ' + str(self.visible)


def run_part_1(input_file):
    count = 0
    forest = []
    i = 0

    with open(input_file) as file:
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
            if not forest[i][j].visible:
                forest[i][j].visible = i == 0 or i == len_i-1 or j == 0 or j == len_j-1
            if not forest[i][j].visible:
                # look left
                for k in range(j, -1, -1):
                    if forest[i][j].height > forest[i][k].height:
                        if forest[i][k].visible:
                            forest[i][j].visible = True
                            break
                    else:
                        break
            if not forest[i][j].visible:
                # look right
                for k in range(j, len_j, 1):
                    if forest[i][j].height > forest[i][k].height:
                        if forest[i][k].visible:
                            forest[i][j].visible = True
                            break
                    else:
                        break
            if not forest[i][j].visible:
                # look up
                for k in range(i, -1, -1):
                    if forest[i][j].height > forest[k][j].height:
                        if forest[k][j].visible:
                            forest[i][j].visible = True
                            break
                    else:
                        break
            if not forest[i][j].visible:
                # look down
                for k in range(i, len_i, 1):
                    if forest[i][j].height > forest[k][j].height:
                        if forest[k][j].visible:
                            forest[i][j].visible = True
                            break
                    else:
                        break
            if forest[i][j].visible:
                count += 1

    print(count)


if __name__ == '__main__':
    run_part_1("./input.txt")
