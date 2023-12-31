import logging
import sys
from typing import Any

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def sanity_check(line: str) -> bool:
    """This evaluates entry line for data sanity
    Args:
        line: a string containing match results
    Return:
        True or False
    """
    line_list = line.split(",")
    if len(line_list) != 2:
        return False

    for team in line_list:
        score = team.split(" ").pop()
        try:
            int(score)
        except ValueError:
            logging.debug(f"The input score '{team}' failed sanity check")
            return False
    return True


def transform_to_dict(match: str) -> dict:
    """Transforms a match string into a dictionary.

    Args:
        match: A string representing a match.

    Returns:
        A dictionary representing the match, with team names as keys and scores as values.
    """

    line = [x.strip(" ") for x in match.split(",")]
    return dict(x.rsplit(" ", 1) for x in line)


def display_logtable(log: list[Any]):
    """This displays the log table

    Args:
        log: a list of team and points
    """
    prev_score_ref = prev_index_ref = 0
    for entry in log:
        ix = prev_index_ref if entry[1] == prev_score_ref else prev_index_ref + 1
        print(f"{ix}.  {entry[0]}, {entry[1]} pts")
        prev_score_ref, prev_index_ref = entry[1], ix
