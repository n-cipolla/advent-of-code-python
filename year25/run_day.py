import importlib
import sys


def run_day(day_number: int, part_number: int) -> None:
    day_str = f"day{day_number:02d}"
    try:
        module = importlib.import_module(f"days.{day_str}")
        if part_number == 1 and hasattr(module, "part1"):
            module.part1()
        elif part_number == 2 and hasattr(module, "part2"):
            module.part2()
        else:
            print(f"No part1() or part2() methods found for {day_str}.py")
    except ModuleNotFoundError:
        print(f"Could not find module: days/{day_str}.py")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python run_day.py <day_number> <part_number>")
    else:
        run_day(int(sys.argv[1]), int(sys.argv[2]))
