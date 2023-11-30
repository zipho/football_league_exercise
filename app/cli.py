"""Console script for app."""
import dataclasses
import sys
import click
from app.match import Match
import logging
import sys
from app.helper import sanity_check, transform_to_dict, display_logtable
import collections, functools, operator
from typing import Any

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


@click.command()
@click.argument("fixture_file", type=click.File("r"))
def main(fixture_file):
    """Console script for app.

    Arguments:
        fixture_file: File object passed as argument via command prompt
    """
    league_log = []
    for line in fixture_file:
        if sanity_check(line.strip()):
            try:
                handle_match(line.strip(), league_log)
            except Exception as e:
                logging.error(f"Error while processing the match input: {e}")
                e.add_note("Error while processing the match")
                raise
    value_sort = handle_sort(league_log) if league_log else []
    display_logtable(value_sort)


def handle_match(line: str, league_log: list):
    """This handles the allocation of outcomes for each team

    Arguments:
        line: a line entry on the match results log table
        league_log: a list of dictionaries that has point allocation for each match
    """
    result_dict = transform_to_dict(line)
    match = Match(result_dict)
    if match.outcome.name == "DRAW":
        for team in list(result_dict.keys()):
            league_log.append({team: 1})
    else:
        league_log.append({match.winner: 3})
        league_log.append({match.looser: 0})


def handle_sort(league_log: list) -> list[Any]:
    """This handles the calculation and sorting of overall results

    Arguments:
        league_log: a list of the dictionaries containing the points allocation for matches
    """
    counter = collections.Counter()
    for entry in league_log:
        counter.update(entry)
    results = dict(counter)
    key_sort = sorted(results.items(), key=lambda x: x[0], reverse=False)
    value_sort = sorted(key_sort, key=lambda x: x[1], reverse=True)
    return value_sort


if __name__ == "__main__":
    main()
