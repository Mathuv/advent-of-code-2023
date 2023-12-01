import sys
from pathlib import Path
from typing import List


def parse_input(puzzle_input_file_path: Path) -> List[str]:
    """Parse input data."""

    text = puzzle_input_file_path.read_text().strip()

    return text.splitlines()


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1: What is the sum of all of the calibration values?
    """

    data: List[str] = parse_input(puzzle_input_file_path)

    sum_cal = 0
    d1: str = ""
    d2: str = ""
    for line in data:
        for char in line:
            if char.isdigit():
                d1 = char
                break

        for char in line[::-1]:
            if char.isdigit():
                d2 = char
                break

        sum_cal += int(d1 + d2)

    return sum_cal


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    data: List[str] = parse_input(puzzle_input_file_path)

    return 0


def solve_puzzle(puzzle_input_file_path: Path):
    """
    Solve the Advent of Code puzzle of the day.
    """

    solution_1 = solve_part_1(puzzle_input_file_path)
    solution_2 = solve_part_2(puzzle_input_file_path)

    return solution_1, solution_2


if __name__ == "__main__":
    # Read input data
    puzzle_input_file_path: Path = Path(sys.argv[1])

    # Solve the puzzle
    solution_1, solution_2 = solve_puzzle(puzzle_input_file_path)

    # Print the solutions
    print(f"Solution 1: {solution_1}")
    print(f"Solution 2: {solution_2}")
