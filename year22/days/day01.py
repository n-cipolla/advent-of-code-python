from tools import read_strings_from_file


def part1():
    puzzle_input = read_strings_from_file('day01.txt')

    counter = 1
    elves_and_counts = dict()
    current = list()

    for line in puzzle_input:
        if line != "":
            current.append(int(line))
        else:
            elves_and_counts[counter] = current
            current = list()
            counter += 1

    elves_and_sums = dict()
    for elf in elves_and_counts:
        elves_and_sums[elf] = sum(elves_and_counts[elf])

    max = 0
    big_elf = 0
    for elf in elves_and_sums:
        if max < elves_and_sums[elf]:
            max = elves_and_sums[elf]
            big_elf = elf

    print(max)


def part2():
    puzzle_input = read_strings_from_file('day01.txt')

    counter = 1
    elves_and_counts = dict()
    current = list()

    for line in puzzle_input:
        if line != "":
            current.append(int(line))
        else:
            elves_and_counts[counter] = current
            current = list()
            counter += 1

    elves_and_sums = dict()
    for elf in elves_and_counts:
        elves_and_sums[elf] = sum(elves_and_counts[elf])

    total = 0
    max = 0
    big_elf = 0
    for elf in elves_and_sums:
        if max < elves_and_sums[elf]:
            max = elves_and_sums[elf]
            big_elf = elf

    total += max
    elves_and_sums[big_elf] = 0

    max = 0
    big_elf = 0
    for elf in elves_and_sums:
        if max < elves_and_sums[elf]:
            max = elves_and_sums[elf]
            big_elf = elf

    total += max
    elves_and_sums[big_elf] = 0

    max = 0
    big_elf = 0
    for elf in elves_and_sums:
        if max < elves_and_sums[elf]:
            max = elves_and_sums[elf]
            big_elf = elf

    total += max
    elves_and_sums[big_elf] = 0

    print(total)
