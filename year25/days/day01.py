from tools import read_strings_from_file

def part1():
    puzzle_input = read_strings_from_file('day01.txt')

    index = 50
    count = 0

    for line in puzzle_input:
        direction = line[0]
        if direction == 'L':
            index -= int(line[1:])
            while index < 0:
                index += 100
        elif direction == 'R':
            index += int(line[1:])
            while index > 99:
                index -= 100

        if index == 0:
            count += 1

    print(count)

def part2():
    puzzle_input = read_strings_from_file('test01-2.txt')

    index = 50
    count = 0

    for line in puzzle_input:
        direction = line[0]

        if direction == 'L':
            index -= int(line[1:]) % 100
            while index < 0:
                index += 100
            count += 1 * (int(line[1:]) // 100)

        elif direction == 'R':
            index += int(line[1:])
            while index > 99:
                index -= 100
                # count += 1
            count += 1 * (int(line[1:]) // 100)

        return index



        # 6967 too high

    print("Count:", count)
