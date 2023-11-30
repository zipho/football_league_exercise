import pytest
from app.helper import transform_to_dict


# Happy path tests with various realistic test values
@pytest.mark.parametrize(
    "input_str, expected_dict",
    [
        # Test ID: #1
        ("key1 value1, key2 value2", {"key1": "value1", "key2": "value2"}),
        # Test ID: #2
        ("status OK, code 200", {"status": "OK", "code": "200"}),
        # Test ID: #3
        ("error None, message Success", {"error": "None", "message": "Success"}),
        # Test ID: #4
        ("  space before,space after ", {"space before": "", "space after": ""}),
        # Test ID: #5
        ("single-entry value", {"single-entry": "value"}),
    ],
    ids=[
        "happy-case-normal",
        "happy-case-status-code",
        "happy-case-error-message",
        "happy-case-spaces",
        "happy-case-single-entry",
    ],
)
def test_transform_to_dict_happy_path(input_str, expected_dict):
    # Act
    result = transform_to_dict(input_str)

    # Assert
    assert result == expected_dict, f"Expected {expected_dict}, got {result}"


# Edge cases
@pytest.mark.parametrize(
    "input_str, expected_dict",
    [
        # Test ID: #6
        ("", {}),
        # Test ID: #7
        ("key1 value1 key2 value2", {"key1": "value1 key2 value2"}),
        # Test ID: #8
        ("key1, key2 value2", {"key1": "", "key2": "value2"}),
        # Test ID: #9
        ("key1 value1 key2, value2", {"key1": "value1 key2", "value2": ""}),
    ],
    ids=[
        "edge-case-empty",
        "edge-case-no-comma",
        "edge-case-missing-value",
        "edge-case-missing-value-with-comma",
    ],
)
def test_transform_to_dict_edge_cases(input_str, expected_dict):
    # Act
    result = transform_to_dict(input_str)

    # Assert
    assert result == expected_dict, f"Expected {expected_dict}, got {result}"


# Error cases
@pytest.mark.parametrize(
    "input_str, error_type",
    [
        # Test ID: #10
        (None, TypeError),
        # Test ID: #11
        (123, AttributeError),
        # Test ID: #12
        (["key1 value1, key2 value2"], TypeError),
    ],
    ids=["error-case-none", "error-case-int", "error-case-list"],
)
def test_transform_to_dict_error_cases(input_str, error_type):
    # Act / Assert
    with pytest.raises(error_type):
        transform_to_dict(input_str)
