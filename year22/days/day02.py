from tools import read_strings_from_file


def part1():
    my_input = read_strings_from_file('day02.txt')
    # elf_conversions = {"A": "rock", "B": "paper", "C": "scissors"}
    # my_conversions = {"X": "rock", "Y": "paper", "Z": "scissors"}

    # points as follows:
    # win = 6
    # tie = 3
    # loss = 0

    # rock = 1
    # paper = 2
    # scissors = 3

    total = 0
    for string in my_input:
        if string.startswith("A"):
            if string.endswith("X"):
                total += 3 + 1
            elif string.endswith("Y"):
                total += 6 + 2
            else:
                total += 0 + 3
        elif string.startswith("B"):
            if string.endswith("X"):
                total += 0 + 1
            elif string.endswith("Y"):
                total += 3 + 2
            else:
                total += 6 + 3
        elif string.startswith("C"):
            if string.endswith("X"):
                total += 6 + 1
            elif string.endswith("Y"):
                total += 0 + 2
            else:
                total += 3 + 3

    print(total)


def part2():
    my_input = read_strings_from_file('day02.txt')
    total = 0

    # new rules     points:     points:
    # X = lose      win = 6     rock = 1
    # Y = tie       tie = 3     paper = 2
    # Z = win       loss = 0    scissors = 3

    for string in my_input:
        if string.startswith("A"):
            if string.endswith("X"):
                total += 0 + 3
            elif string.endswith("Y"):
                total += 3 + 1
            else:
                total += 6 + 2
        elif string.startswith("B"):
            if string.endswith("X"):
                total += 0 + 1
            elif string.endswith("Y"):
                total += 3 + 2
            else:
                total += 6 + 3
        elif string.startswith("C"):
            if string.endswith("X"):
                total += 0 + 2
            elif string.endswith("Y"):
                total += 3 + 3
            else:
                total += 6 + 1

    print(total)
