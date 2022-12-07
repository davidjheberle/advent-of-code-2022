class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size


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
                size = data[0]
                file_name = data[1]
                current_directory.children.append(File(file_name, size))

    return root_directory


def run_part_1(input_file):
    print(parse_input(input_file))


if __name__ == '__main__':
    run_part_1("./input.txt")
