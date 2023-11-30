import pytest
from app.helper import sanity_check


# Happy path tests with various realistic test values
@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("TeamA 1,TeamB 2", True, "id=HappyPath1"),
        ("Winners 10,Losers 0", True, "id=HappyPath2"),
        ("Draw 3,Draw 3", True, "id=HappyPath3"),
        ("Underdogs 2,Champions 2", True, "id=HappyPath4"),
    ],
)
def test_sanity_check_happy_path(test_input, expected):
    # Act
    result = sanity_check(test_input)

    # Assert
    assert result == expected


# Edge cases
@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("", False, "id=EdgeCaseEmptyString"),
        ("TeamA 1,", False, "id=EdgeCaseMissingSecondTeam"),
        (",TeamB 2", False, "id=EdgeCaseMissingFirstTeam"),
        ("TeamA 1 TeamB 2", False, "id=EdgeCaseNoComma"),
        ("TeamA,TeamB", False, "id=EdgeCaseNoScores"),
        ("  ", False, "id=EdgeCaseOnlySpaces"),
        ("TeamA 1,TeamB", False, "id=EdgeCaseSecondTeamNoScore"),
        ("TeamA,TeamB 2", False, "id=EdgeCaseFirstTeamNoScore"),
    ],
)
def test_sanity_check_edge_cases(test_input, expected):
    # Act
    result = sanity_check(test_input)

    # Assert
    assert result == expected


# Error cases
@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("TeamA one,TeamB two", False, "id=ErrorCaseNonNumericScore"),
        ("TeamA -1,TeamB 2", False, "id=ErrorCaseNegativeScore"),
        ("TeamA 1.5,TeamB 2", False, "id=ErrorCaseDecimalScore"),
        ("TeamA 1,TeamB two", False, "id=ErrorCaseSecondTeamNonNumeric"),
        ("TeamA one,TeamB 2", False, "id=ErrorCaseFirstTeamNonNumeric"),
        ("TeamA 1 1,TeamB 2", False, "id=ErrorCaseExtraNumberInScore"),
        ("TeamA,TeamB 2 2", False, "id=ErrorCaseExtraNumberInSecondTeamScore"),
        ("TeamA 1,TeamB 2 extra", False, "id=ErrorCaseExtraTextAfterScore"),
    ],
)
def test_sanity_check_error_cases(test_input, expected):
    # Act
    result = sanity_check(test_input)

    # Assert
    assert result == expected
