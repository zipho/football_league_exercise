import logging
import sys

from enum import Enum

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class MatchOutcome(Enum):
    DRAW = 0
    DECIDED = 1


class Match:
    """Match class with common methods and attributes to establish points"""

    def __init__(self, results):
        self._team = None
        self.results = results
        self._winner = self._looser = self._outcome = None

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team = value

    @property
    def winner(self):
        if self._outcome.name == "DECIDED":
            self._winner = max(self.results, key=self.results.get)
        return self._winner

    @property
    def looser(self):
        if self._outcome.name == "DECIDED":
            self._looser = min(self.results, key=self.results.get)
        return self._looser

    @property
    def outcome(self):
        final_scores = list(self.results.values())
        if final_scores:
            if final_scores[0] == final_scores[1]:
                self._outcome = MatchOutcome(0)
            else:
                self._outcome = MatchOutcome(1)
        return self._outcome
