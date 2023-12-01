import sys
from pathlib import Path
from typing import List, Dict

def parse_input(puzzle_input_file_path: Path) -> List[str]:
    """Parse input data and return as a list of lines."""
    return puzzle_input_file_path.read_text().strip().splitlines()

def replace_first_and_last_occurrence_of_word_with_digit(line: str, word_to_digit_map: Dict[str, str]) -> str:
    """Replace the first occurrence of the word with the smallest position and 
    the last occurrence of the word with the latest position."""

    # Find the first occurrence
    first_occurrence_pos = len(line)
    first_word_to_replace = None
    for word in word_to_digit_map:
        pos = line.find(word)
        if 0 <= pos < first_occurrence_pos:
            first_occurrence_pos = pos
            first_word_to_replace = word

    # Replace the first occurrence
    if first_word_to_replace:
        line = line.replace(first_word_to_replace, word_to_digit_map[first_word_to_replace], 1)

    # Find the last occurrence
    last_occurrence_pos = -1
    last_word_to_replace = None
    for word in word_to_digit_map:
        pos = line.rfind(word)
        if pos > last_occurrence_pos:
            last_occurrence_pos = pos
            last_word_to_replace = word

    # Replace the last occurrence
    if last_word_to_replace:
        line = line[:last_occurrence_pos] + line[last_occurrence_pos:].replace(last_word_to_replace, word_to_digit_map[last_word_to_replace], 1)

    print(line)

    return line

def calc_sum_of_calibrations(data: List[str]) -> int:
    """Calculate the sum of calibrations."""
    sum_cal = 0
    for line in data:
        digits = [char for char in line if char.isdigit()]
        if digits:
            cal_val = int(digits[0] + digits[-1])
            sum_cal += cal_val
    return sum_cal

def solve_part_1(puzzle_input_file_path: Path) -> int:
    """Solve part 1: What is the sum of all of the calibration values?"""
    data = parse_input(puzzle_input_file_path)
    return calc_sum_of_calibrations(data)

def solve_part_2(puzzle_input_file_path: Path) -> int:
    """Solve part 2 with specific word replacement."""
    word_to_digit_map = {
        "oneight": "18", "twone": "21", "eightwo": "82", 
        "eighthree": "83",
        "sevenine": "79", "fiveight": "58", "nineight": "98", "threeight": "38",
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    }
    data = parse_input(puzzle_input_file_path)
    data = [replace_first_and_last_occurrence_of_word_with_digit(line, word_to_digit_map) for line in data]
    # print(data)
    return calc_sum_of_calibrations(data)

def solve_puzzle(puzzle_input_file_path: Path):
    """Solve the Advent of Code puzzle of the day."""
    solution_1 = solve_part_1(puzzle_input_file_path)
    solution_2 = solve_part_2(puzzle_input_file_path)
    return solution_1, solution_2

if __name__ == "__main__":
    puzzle_input_file_path = Path(sys.argv[1])
    solution_1, solution_2 = solve_puzzle(puzzle_input_file_path)
    print(f"Solution 1: {solution_1}\nSolution 2: {solution_2}")
