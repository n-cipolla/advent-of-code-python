from collections import deque

from tools import read_strings_from_file_whitespace


def part1():
    lines = read_strings_from_file_whitespace("day05.txt")

    num_crates = 0
    instruction_start_line = 1
    for line in lines:
        instruction_start_line += 1
        if line.startswith(" 1"):
            num_crates = int(line[len(line) - 1])
            break

    crates = [deque() for _ in range(num_crates)]

    counter = 0
    for line in lines:
        if counter == instruction_start_line - 2:
            break
        else:
            char_pos = 0
            for char in line:
                if char.isalpha():
                    crates[char_pos // 4].append(char)
                char_pos += 1
        counter += 1

    for d in crates:
        d.reverse()

    for i in range(instruction_start_line, len(lines)):
        count = int(lines[i].split(" ")[1])
        from_stack = int(lines[i].split(" ")[3]) - 1
        to_stack = int(lines[i].split(" ")[5]) - 1

        for j in range(count):
            crates[to_stack].append(crates[from_stack].pop())

    for crate in crates:
        print(crate.pop(), end="")


def part2():
    lines = read_strings_from_file_whitespace("day05.txt")

    num_crates = 0
    instruction_start_line = 1
    for line in lines:
        instruction_start_line += 1
        if line.startswith(" 1"):
            num_crates = int(line[len(line) - 1])
            break

    crates = [deque() for _ in range(num_crates)]

    counter = 0
    for line in lines:
        if counter == instruction_start_line - 2:
            break
        else:
            char_pos = 0
            for char in line:
                if char.isalpha():
                    crates[char_pos // 4].append(char)
                char_pos += 1
        counter += 1

    for d in crates:
        d.reverse()

    for i in range(instruction_start_line, len(lines)):
        count = int(lines[i].split(" ")[1])
        from_stack = int(lines[i].split(" ")[3]) - 1
        to_stack = int(lines[i].split(" ")[5]) - 1

        tmp = deque()
        for j in range(count):
            tmp.append(crates[from_stack].pop())

        for j in range(len(tmp)):
            crates[to_stack].append(tmp.pop())

    for crate in crates:
        print(crate.pop(), end="")
