import logging
import sys

from enum import Enum

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class MatchOutcome(Enum):
    """Enum class representing the outcome of a match.

    Attributes:
        DRAW: Represents a draw outcome.
        DECIDED: Represents a decided outcome.
    """

    DRAW = 0
    DECIDED = 1


class Match:
    """Class representing a match.

    Attributes:
        results: A dictionary containing the results of the match.
        team: The team associated with the match.
        winner: The winning team of the match.
        looser: The losing team of the match.
        outcome: The outcome of the match.

    """

    def __init__(self, results):
        self._team = None
        self.results = results
        self._winner = self._looser = self._outcome = None

    @property
    def team(self):
        """Getter method for the team attribute.

        Returns:
            The team associated with the match.
        """
        return self._team

    @team.setter
    def team(self, value):
        """Setter method for the team attribute.

        Args:
            value: The value to set as the team.
        """
        self._team = value

    @property
    def winner(self):
        """Getter method for the winner attribute.

        Returns:
            The winning team of the match.
        """
        if self._outcome.name == "DECIDED":
            self._winner = max(self.results, key=self.results.get)
        return self._winner

    @property
    def looser(self):
        """Getter method for the looser attribute.

        Returns:
            The losing team of the match.
        """
        if self._outcome.name == "DECIDED":
            self._looser = min(self.results, key=self.results.get)
        return self._looser

    @property
    def outcome(self):
        """Getter method for the outcome attribute.

        Returns:
            The outcome of the match.
        """
        if final_scores := list(self.results.values()):
            if final_scores[0] == final_scores[1]:
                self._outcome = MatchOutcome(0)
            else:
                self._outcome = MatchOutcome(1)
        return self._outcome
