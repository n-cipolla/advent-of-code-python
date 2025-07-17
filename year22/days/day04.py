from tools import read_strings_from_file


def part1():
    input = read_strings_from_file('day04.txt')

    count = 0

    for line in input:
        first = line.split(",")[0]
        second = line.split(",")[1]

        f_lower = int(first.split("-")[0])
        f_upper = int(first.split("-")[1])

        s_lower = int(second.split("-")[0])
        s_upper = int(second.split("-")[1])

        if f_lower >= s_lower and f_upper <= s_upper:  # first contained within second
            count += 1
        elif s_lower >= f_lower and s_upper <= f_upper:  # second contained within first
            count += 1

    print(count)


def part2():
    input = read_strings_from_file('day04.txt')
    count = 0

    for line in input:
        first = line.split(",")[0]
        second = line.split(",")[1]

        f_lower = int(first.split("-")[0])
        f_upper = int(first.split("-")[1])

        s_lower = int(second.split("-")[0])
        s_upper = int(second.split("-")[1])

        if s_lower <= f_lower <= s_upper:
            count += 1
        elif f_lower <= s_lower <= f_upper:
            count += 1
        elif s_lower <= f_upper <= s_upper:
            count += 1
        elif f_lower <= s_upper <= f_upper:
            count += 1

    print(count)
