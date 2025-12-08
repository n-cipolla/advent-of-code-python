from tools import read_strings_from_file
from tqdm import tqdm


puzzle_input = read_strings_from_file("day03.txt")


def part1():
    total = 0
    for line in puzzle_input:
        max = 0
        for i in range(len(line)-1):
            for j in range(i+1, len(line)):
                number = line[i] + line[j]
                if int(number) > max:
                    max = int(number)

        total += max

    print(total)


def part2():
    total = 0
    print(total)
