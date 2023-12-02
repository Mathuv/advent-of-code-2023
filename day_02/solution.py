import sys
from pathlib import Path
from pprint import pprint
from typing import List

RED = "red"
GREEN = "green"
BLUE = "blue"

BAG_CONTENTS = {
    RED: 12,
    GREEN: 13,
    BLUE: 14,
}


def parse_input(puzzle_input_file_path: Path) -> List[str]:
    """Parse input data."""

    text = puzzle_input_file_path.read_text().strip()

    return text.splitlines()


def transform_input(data: List[str]):
    """
    Transform input data into dictionary of game_ids and reveals
    {
        game_id: [
            {
                color: count,
                ...
            },  # reveal 1
            {
                color: count,
                ...
            },  # reveal 2
            ...
        ],
        ...

    }
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

    # pprint(result)
    return result


def is_reveal_possible(bag_contents: dict, reveal: dict):
    """
    Check if reveal is possible
    """
    return all(bag_contents.get(color, 0) >= count for color, count in reveal.items())


def find_some_of_possible_game_ids(bag_contents: dict, games: dict):
    """
    Find some of possible game ids
    """
    sum_ids = 0
    for game_id, reveals in games.items():
        if all(is_reveal_possible(bag_contents, reveal) for reveal in reveals):
            sum_ids += game_id
    return sum_ids


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    """

    data: List[str] = parse_input(puzzle_input_file_path)
    games = transform_input(data)
    return find_some_of_possible_game_ids(BAG_CONTENTS, games)


def find_min_count_reqired_for_color_in_game(reveals: list) -> dict:
    """
    Find max count reqired for color in game
    """
    min_count_map: dict = {
        RED: 0,
        GREEN: 0,
        BLUE: 0,
    }
    for reveal in reveals:
        if reveal.get(RED, 0) > min_count_map[RED]:
            min_count_map[RED] = reveal[RED]
        if reveal.get(GREEN, 0) > min_count_map[GREEN]:
            min_count_map[GREEN] = reveal[GREEN]
        if reveal.get(BLUE, 0) > min_count_map[BLUE]:
            min_count_map[BLUE] = reveal[BLUE]

    # pprint(min_count_map)
    return min_count_map


def find_sum_of_power_of_sets(games: dict) -> int:
    """
    Find sum of power of sets
    """
    sum_of_power = 0
    for reveals in games.values():
        min_count_map: dict = find_min_count_reqired_for_color_in_game(reveals)
        sum_of_power += min_count_map[RED] * min_count_map[GREEN] * min_count_map[BLUE]
    return sum_of_power


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    data: List[str] = parse_input(puzzle_input_file_path)
    games = transform_input(data)
    return find_sum_of_power_of_sets(games)


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
