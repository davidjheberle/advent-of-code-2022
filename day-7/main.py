class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


class Directory:

    def __init__(self, name, parent, children):
        self.name = name
        self.parent = parent
        self.children = children

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def get_size(self):
        size = 0
        for child in self.children:
            size += child.get_size()
        return size


def agg_size(directory, limit, size):
    directory_size = directory.get_size()
    if directory_size <= limit:
        size += directory_size
    for child in directory.children:
        if isinstance(child, Directory):
            size = agg_size(child, limit, size)
    return size


def find_dir(directory, minimum, current):
    directory_size = directory.get_size()
    if minimum <= directory_size < current.get_size():
        current = directory
    for child in directory.children:
        if isinstance(child, Directory):
            current = find_dir(child, minimum, current)
    return current


def parse_input(input_file):
    root_directory = Directory('/', None, [])
    current_directory = None

    with open(input_file) as file:
        for line in file:
            data = line.strip().split()
            if data[0] == '$':
                command = data[1]
                if command == 'cd':
                    directory = data[2]
                    if directory == '..':
                        current_directory = current_directory.parent
                    elif current_directory is None:
                        current_directory = root_directory
                    else:
                        current_directory = current_directory.get_child(directory)
            elif data[0] == 'dir':
                directory = data[1]
                current_directory.children.append(Directory(directory, current_directory, []))
            else:
                size = int(data[0])
                file_name = data[1]
                current_directory.children.append(File(file_name, size))

    return root_directory


def run_part_1(input_file):
    tree = parse_input(input_file)
    print(agg_size(tree, 100000, 0))


def run_part_2(input_file):
    tree = parse_input(input_file)
    space = 30000000 - (70000000 - tree.get_size())
    print(find_dir(tree, space, tree).get_size())


if __name__ == '__main__':
    run_part_1("./input.txt")
    run_part_2("./input.txt")
