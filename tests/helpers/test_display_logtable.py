import pytest
from app.helper import display_logtable
from io import StringIO
import sys


# Redirecting print statements to a StringIO object for assertion
@pytest.fixture
def capture_print():
    new_out = StringIO()
    sys.stdout = new_out
    yield new_out
    sys.stdout = sys.__stdout__


# Parametrized test cases for happy path, edge cases, and error cases
@pytest.mark.parametrize(
    "test_input,expected_output",
    [
        # Happy path tests
        (
            pytest.param(
                [("Team A", 10), ("Team B", 8), ("Team C", 10)],
                "1.  Team A, 10 pts\n2.  Team B, 8 pts\n1.  Team C, 10 pts\n",
                id="happy_path_same_scores",
            )
        ),
        (
            pytest.param(
                [("Team A", 3)], "1.  Team A, 3 pts\n", id="happy_path_single_entry"
            )
        ),
        (
            pytest.param(
                [("Team A", 10), ("Team B", 8), ("Team C", 6)],
                "1.  Team A, 10 pts\n2.  Team B, 8 pts\n3.  Team C, 6 pts\n",
                id="happy_path_decreasing_scores",
            )
        ),
        # Edge cases
        (pytest.param([], "", id="edge_case_empty_log")),
        (
            pytest.param(
                [("Team A", 10)] * 5,
                "1.  Team A, 10 pts\n" * 5,
                id="edge_case_identical_entries",
            )
        ),
        # Error cases
        (
            pytest.param(
                [("Team A", "ten")],
                pytest.raises(TypeError),
                id="error_case_non_integer_score",
            )
        ),
        (
            pytest.param(
                [12345], pytest.raises(TypeError), id="error_case_non_iterable_entry"
            )
        ),
        (pytest.param([()], pytest.raises(IndexError), id="error_case_empty_tuple")),
    ],
)
def test_display_logtable(test_input, expected_output, capture_print):
    # Act
    display_logtable(test_input)

    # Assert
    if isinstance(expected_output, str):
        output = capture_print.getvalue()
        assert output == expected_output
    else:
        with expected_output:
            display_logtable(test_input)
