import sys
from pathlib import Path
from pprint import pprint
from typing import List

import numpy as np

# REFACTOR for readability
# Set print options
# np.set_printoptions(threshold=np.inf)

# Constants
SYMBOL_CODE = -1
EMPTY_CODE = -2


def parse_input(puzzle_input_file_path: Path) -> List[str]:
    """Parse input data."""

    text = puzzle_input_file_path.read_text().strip()

    return text.splitlines()


def get_adjacent_elements(arr: np.ndarray, row: int, col: int):
    rows, cols = arr.shape

    row_start = max(0, row - 1)
    row_end = min(row + 2, rows)
    col_start = max(0, col - 1)
    col_end = min(col + 2, cols)

    # Extract the subarray including adjacent elements
    sub_arr: np.ndarray = arr[row_start:row_end, col_start:col_end]

    return sub_arr[sub_arr != arr[row, col]]


def load_data_into_numpy_array(lines: List[str]) -> np.ndarray:
    """
    Load data into a numpy array.

    Data:
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    """

    num_rows: int = len(lines)
    num_cols: int = len(lines[0])

    grid = np.zeros((num_rows, num_cols), dtype="int8")
    # replace all zeros with -2
    grid[grid == 0] = EMPTY_CODE 

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char != ".":
                num = int(char) if char.isdigit() else SYMBOL_CODE 
                grid[row, col] = num

    return grid


def find_numbers_adjacent_to_symbols(grid: np.ndarray) -> List[int]:
    """
    Find numbers adjacent to symbols.

    Data:
    [[ 4  6  7 -2 -2  1  1  4 -2 -2]
     [-2 -2 -2 -1 -2 -2 -2 -2 -2 -2]
     [-2 -2  3  5 -2 -2  6  3  3 -2]
     [-2 -2 -2 -2 -2 -2 -1 -2 -2 -2]
     [ 6  1  7 -1 -2 -2 -2 -2 -2 -2]
     [-2 -2 -2 -2 -2 -1 -2  5  8 -2]
     [-2 -2  5  9  2 -2 -2 -2 -2 -2]
     [-2 -2 -2 -2 -2 -2  7  5  5 -2]
     [-2 -2 -2 -1 -2 -1 -2 -2 -2 -2]
     [-2  6  6  4 -2  5  9  8 -2 -2]]
    """

    numbers: List[int] = []
    # Find all numbers adjacent (vertically or horizontally or diagonally) to -1
    for row in range(grid.shape[0]):
        numbers_in_row: List[int] = []
        is_part_no: bool = False
        num = ""
        for col in range(grid.shape[1]):
            if grid[row, col] not in [SYMBOL_CODE, EMPTY_CODE]:
                num = num + str(grid[row, col])

                adjacent_elements = get_adjacent_elements(grid, row, col)
                # check if any of the adjacent elements is -1
                if SYMBOL_CODE in adjacent_elements:
                    is_part_no = True

            else:
                if num and is_part_no:
                    numbers_in_row.append(int(num))
                num = ""
                is_part_no = False
        if num and is_part_no:
            numbers_in_row.append(int(num))
        num = ""
        is_part_no = False
        numbers.append(numbers_in_row) if numbers_in_row else None

    return numbers


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    """

    data: List[str] = parse_input(puzzle_input_file_path)
    grid = load_data_into_numpy_array(data)
    numbers = find_numbers_adjacent_to_symbols(grid)

    return sum(map(sum, numbers))


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
