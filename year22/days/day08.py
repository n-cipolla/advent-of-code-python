from tools import read_strings_from_file

import numpy as np


def part1():
    input = read_strings_from_file("day08.txt")

    trees = np.zeros((len(input), len(input[0])))
    for i in range(len(input)):
        for j in range(len(input[0])):
            trees[i][j] = input[i][j]

    visible = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if i == 0 or i == len(input) - 1 or j == 0 or j == len(input[0]) - 1:
                visible += 1
            else:
                up = True
                down = True
                left = True
                right = True
                for u in range(i):
                    if not trees[u][j] < trees[i][j]:
                        up = False

                for d in range(i + 1, len(input)):
                    if not trees[d][j] < trees[i][j]:
                        down = False

                for l in range(j):
                    if not trees[i][l] < trees[i][j]:
                        left = False

                for r in range(j + 1, len(input[0])):
                    if not trees[i][r] < trees[i][j]:
                        right = False

                if up or down or left or right:
                    visible += 1

    print(visible)


def part2():
    input = read_strings_from_file("day08.txt")

    trees = np.zeros((len(input), len(input[0])))
    for i in range(len(input)):
        for j in range(len(input[0])):
            trees[i][j] = input[i][j]

    max_scenic_score = 0

    for i in range(len(input)):
        for j in range(len(input[0])):
            if i == 0 or i == len(input) - 1 or j == 0 or j == len(input[0]) - 1:
                scenic_score = 0
            else:
                up = 0
                down = 0
                left = 0
                right = 0
                for u in range(i-1, -1, -1):
                    if trees[u][j] < trees[i][j]:
                        up += 1
                    elif trees[u][j] >= trees[i][j]:
                        up += 1
                        break

                for d in range(i + 1, len(input)):
                    if trees[d][j] < trees[i][j]:
                        down += 1
                    elif trees[d][j] >= trees[i][j]:
                        down += 1
                        break

                for l in range(j-1, -1, -1):
                    if trees[i][l] < trees[i][j]:
                        left += 1
                    elif trees[i][l] >= trees[i][j]:
                        left += 1
                        break

                for r in range(j + 1, len(input[0])):
                    if trees[i][r] < trees[i][j]:
                        right += 1
                    elif trees[i][r] >= trees[i][j]:
                        right += 1
                        break

                scenic_score = up * down * left * right

            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    print(max_scenic_score)
