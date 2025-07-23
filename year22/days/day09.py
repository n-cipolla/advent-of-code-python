from tools import read_strings_from_file

import numpy as np


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def translate_x(self, dx):
        self.x += dx

    def translate_y(self, dy):
        self.y += dy

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def within_one(self, other):
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        return dx <= 1 and dy <= 1


def part1():
    input = read_strings_from_file("test09.txt")
    tail_visited = set()
    head = Point(0, 0)
    tail = Point(0, 0)
    tail_visited.add(tail)
    for line in input:
        direction = line.split(" ")[0]
        amount = int(line.split(" ")[1])

        if direction == "R":
            head.translate_x(amount)
            if tail.y == head.y:
                for i in range(amount - 1):
                    tail_visited.add(tail.translate_x(1))
            else:
                if head.y < tail.y:  # Head below tail
                    tail.translate_y(-1)
                    tail.translate_x(1)
                    tail_visited.add(tail)
                else:  # Head above tail
                    tail.translate_y(1)
                    tail.translate_x(1)
                    tail_visited.add(tail)

                for i in range(amount - 2):
                    tail_visited.add(tail.translate_x(1))

        elif direction == "L":
            head.translate_x(-amount)
            if tail.y == head.y:
                for i in range(amount - 1):
                    tail_visited.add(tail.translate_x(-1))
            else:
                if head.y < tail.y:  # Head below tail
                    tail.translate_y(-1)
                    tail.translate_x(-1)
                    tail_visited.add(tail)
                else:  # Head above tail
                    tail.translate_y(1)
                    tail.translate_x(-1)
                    tail_visited.add(tail)

            for i in range(amount - 2):
                tail_visited.add(tail.translate_x(-1))

        elif direction == "U":
            head.translate_y(amount)

        elif direction == "D":
            head.translate_y(-amount)

    for point in tail_visited:
        print(point)

    print(len(tail_visited))


def part2():
    pass
