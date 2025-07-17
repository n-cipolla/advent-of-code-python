from tools import read_strings_from_file

lowercase_letter_to_number = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
                              "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
                              "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
                              "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                              "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
                              "z": 26}

uppercase_letter_to_number = {"A": 27, "B": 28, "C": 29, "D": 30, "E": 31,
                              "F": 32, "G": 33, "H": 34, "I": 35, "J": 36,
                              "K": 37, "L": 38, "M": 39, "N": 40, "O": 41,
                              "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46,
                              "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51,
                              "Z": 52
                              }


def part1():
    my_in = read_strings_from_file('day03.txt')
    total = 0
    for sack in my_in:
        first_half = sack[0:len(sack) // 2]
        second_half = sack[len(sack) // 2:]

        first = {char for char in first_half}
        second = {char for char in second_half}

        first.intersection_update(second)

        if first.issubset(uppercase_letter_to_number.keys()):
            total += uppercase_letter_to_number.get(list(first)[0])
        else:
            total += lowercase_letter_to_number.get(list(first)[0])

    print(total)


def part2():
    my_in = read_strings_from_file('day03.txt')
    total = 0

    counter = 0
    for group in range(len(my_in)//3):
        first = {char for char in my_in[counter]}
        second = {char for char in my_in[counter+1]}
        third = {char for char in my_in[counter+2]}
        counter += 3

        first.intersection_update(second)
        first.intersection_update(third)

        if first.issubset(uppercase_letter_to_number.keys()):
            total += uppercase_letter_to_number.get(list(first)[0])
        else:
            total += lowercase_letter_to_number.get(list(first)[0])

    print(total)
