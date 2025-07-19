from tools import read_strings_from_file


def part1():
    input = read_strings_from_file('day06.txt')[0]

    counter = 0
    for char in range(len(input)):
        tmp = {c for c in input[char:char+4]}
        if len(tmp) == 4:
            print(tmp)
            break
        counter += 1

    print(counter+4)


def part2():
    input = read_strings_from_file('day06.txt')[0]

    counter = 0
    for char in range(len(input)):
        tmp = {c for c in input[char:char+14]}
        if len(tmp) == 14:
            print(tmp)
            break
        counter += 1

    print(counter+14)
