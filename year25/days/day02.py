from tools import read_strings_from_file
import numpy as np


def part1():
    """
    Returns TRUE if a number contains EXACTLY 1 copy of repeat digits
    """
    def check_valid(number):
        first_half = str(number)[:len(str(number)) // 2]
        second_half = str(number)[len(str(number)) // 2:]

        if first_half == second_half:
            return False

        return True

    puzzle_input = read_strings_from_file("day02.txt")
    ranges = puzzle_input[0].split(",")
    lower = [int(ranges[i].split("-")[0]) for i in range(len(ranges))]
    upper = [int(ranges[i].split("-")[1]) for i in range(len(ranges))]

    invalid = []
    for min, max in zip(lower, upper):
        for num in range(min, max+1, 1):
            if not check_valid(num):
                invalid.append(num)



    print(sum(invalid))

def part2():
    puzzle_input = read_strings_from_file("test02.txt")
    ranges = puzzle_input[0].split(",")
    lower = [int(ranges[i].split("-")[0]) for i in range(len(ranges))]
    upper = [int(ranges[i].split("-")[1]) for i in range(len(ranges))]

    invalid = []
    for min, max in zip(lower, upper):
        for i in range(min, max+1):
            digits = str(i)
            counts = np.zeros(10, dtype = int)
            for num in digits:
                counts[int(num)] += 1


    print(invalid)