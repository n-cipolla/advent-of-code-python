from tools import read_strings_from_file


class Monkey:
    def __init__(self, holding, operation, test, true_throw, false_throw):
        self.holding = holding
        self.operation = operation
        self.test = test
        self.true_throw = true_throw
        self.false_throw = false_throw

    def __str__(self):
        return f"Monkey holding: {self.holding}"

    def __repr__(self):
        return f"Monkey holding: {self.holding}"


def part1():
    input = read_strings_from_file("test11.txt")

    monkeys = []
    for i in range(0, len(input), 7):
        holding = [int(i) for i in input[i + 1].split(": ")[1].split(", ")]
        operation = input[i + 2].split(": ")[1]
        test = input[i + 3].split(": ")[1]
        true_throw = int(input[i + 4].split("monkey")[1])
        false_throw = int(input[i + 5].split("monkey")[1])
        monkeys.append(Monkey(holding, operation, test, true_throw, false_throw))

    for monkey in monkeys:
        operator = monkey.operation.split(" = ")[1][4]
        for item in monkey.holding:
            if monkey.operation.split(" ")[4] == "old":
                value = item
            else:
                value = int(monkey.operation.split(" ")[4])

            if operator == "+":
                item = item + value
            elif operator == "*":
                item = item * value

            item //= 3

            if item % int(monkey.test.split("by ")[1]) == 0:
                monkeys[monkey.true_throw].holding.append(item)
            else:
                monkeys[monkey.false_throw].holding.append(item)

        print(monkey)

    # for monkey in monkeys:
    #     print(monkey)


def part2():
    pass
