from tools import read_strings_from_file

import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)


def part1():
    input = read_strings_from_file("day10.txt")
    x_register = 1
    cycle_count = 1
    sum = 0
    for line in input:
        instruction = line.split(" ")[0]

        if instruction == "addx":
            amount = int(line.split(" ")[1])
            cycle_count += 1
            if (cycle_count - 20) % 40 == 0:
                sum += x_register * cycle_count
                # print(f"1 {cycle_count} : x = {x_register}, increment by: {x_register * cycle_count}")
            cycle_count += 1
            x_register += amount
            if (cycle_count - 20) % 40 == 0:
                sum += x_register * cycle_count
                # print(f"2 {cycle_count} : x = {x_register}, increment by: {x_register * cycle_count}")
        elif instruction == "noop":
            cycle_count += 1
            if (cycle_count - 20) % 40 == 0:
                sum += x_register * cycle_count
                # print(f"3 {cycle_count} : x = {x_register}, increment by: {x_register * cycle_count}")

    print(sum)


def part2():
    input = read_strings_from_file("test10.txt")

    output = np.full((6, 40), "░")

    filler = "█"

    sprite_center = 1

    pixel_counter = 0

    for line in input:
        instruction = line.split(" ")[0]

        if instruction == "addx":
            amount = int(line.split(" ")[1])

            pixel_counter += 1
            pix_row = (pixel_counter + 1) // 40
            pix_col = (pixel_counter - 1) % 40

            sprite_col = sprite_center % 40

            if pix_col-1 <= sprite_col <= pix_col+1:
                output[pix_row, pix_col] = filler

            pixel_counter += 1
            pix_row = (pixel_counter + 1) // 40
            pix_col = (pixel_counter - 1) % 40

            sprite_col = sprite_center % 40

            if pix_col-1 <= sprite_col <= pix_col+1:
                output[pix_row][pix_col] = filler

            sprite_center += amount

        else:
            pixel_counter += 1
            pix_row = (pixel_counter + 1) // 40
            pix_col = (pixel_counter - 1) % 40

            sprite_col = sprite_center % 40

            if pix_col-1 <= sprite_col <= pix_col+1:
                output[pix_row][pix_col] = filler

        for array in output:
            for thing in array:
                print(thing, sep="", end="")
            print("")

        print()
