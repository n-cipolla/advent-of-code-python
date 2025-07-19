from tools import read_strings_from_file


def sum_letter_nodes(node, sum=0):
    """
    Performs a DFS search of all alpha-nodes, summing their contents.
    :param node: The root node.
    :param sum: The sum of all alpha nodes (defaults to 0).
    :return: The sum of all integer values in the tree.
    """
    for child in node.children:
        if isinstance(child.value, int):
            sum += int(child.value)
        else:
            sum += sum_letter_nodes(child, sum)
    return sum


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None
        self.level = 0
        self.max_level = 0

    def add_child(self, child_node):
        """Adds a child node to the current node."""
        self.children.append(child_node)
        child_node.parent = self
        child_node.level = self.level + 1

        current = self
        while current is not None:
            if child_node.level > current.max_level:
                current.max_level = child_node.level
            else:
                break  # no need to keep updating if it's not higher
            if current == current.parent:
                break  # reached root
            current = current.parent

    def has_child(self, child):
        """Returns True if the value is a child of the current node."""
        for c in self.children:
            if c.value == child:
                return True
        return False

    def get_specific(self, value):
        """Returns the node object for a specified value."""
        for c in self.children:
            if c.value == value:
                return c

    def __str__(self, level=0):
        """String representation for printing the tree structure."""
        ret = "   " * level + str(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret


def part1():
    input = read_strings_from_file("test07.txt")

    input.remove("$ cd /")
    input.remove("$ ls")

    root = Node("/")
    current_directory = root
    directory_names = {"/"}
    for i in range(len(input)):
        if input[i].startswith("$"):
            if input[i].endswith("ls"):
                pass
            elif "cd" in input[i]:
                target_directory = input[i].split(" ")[-1]
                if target_directory == "..":
                    current_directory = current_directory.parent
                elif target_directory == "/":
                    current_directory = root
                else:
                    if current_directory.has_child(target_directory):
                        current_directory = current_directory.get_specific(target_directory)
                    else:
                        new_child = Node(target_directory)
                        current_directory.add_child(new_child)

        elif input[i][0].isdigit():
            current_directory.add_child(Node(int(input[i].split(" ")[0])))

        elif input[i][0].isalpha():
            current_directory.add_child(Node(input[i].split(" ")[-1]))
            directory_names.add(input[i].split(" ")[-1])

