import sys
from pathlib import Path
from pprint import pprint
from typing import List


def parse_input(puzzle_input_file_path: Path) -> List[str]:
    """Parse input data."""

    text = puzzle_input_file_path.read_text().strip()

    return text.splitlines()


def transform_input(data: List[str]):
    """
    Transform input data into dictionary of game_ids and reveals
    """
    result = {}
    for line in data:
        game, reveals = line.split(":")
        game_id = int(game.split(" ")[1])
        result[game_id] = []
        for reveal in reveals.split(";"):
            color_dict = {}
            for color in reveal.strip().split(","):
                if color := color.strip():
                    color_dict[color.split(" ")[1]] = int(color.split(" ")[0])
            result[game_id].append(color_dict)

    pprint(result)
    return result


def is_reveal_possible(bag_contents: dict, reveal: dict):
    """
    Check if reveal is possible
    """
    return all(
        bag_contents.get(color, 0) >= count for color, count in reveal.items()
    )


def find_some_of_possible_game_ids(bag_contents: dict, games: dict):
    """
    Find some of possible game ids
    """
    sum = 0
    for game_id, reveals in games.items():
        if all(is_reveal_possible(bag_contents, reveal) for reveal in reveals):
            sum += game_id
    return sum


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    """
    BAG_CONTENTS = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    data: List[str] = parse_input(puzzle_input_file_path)
    games = transform_input(data)
    return find_some_of_possible_game_ids(BAG_CONTENTS, games)


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
