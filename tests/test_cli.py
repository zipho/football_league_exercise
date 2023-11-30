#!/usr/bin/env python

"""Tests for `app` package."""

import pytest

from click.testing import CliRunner
from pytest_datadir.plugin import shared_datadir

from app import cli


@pytest.fixture()
def runner():
    return CliRunner()


@pytest.fixture()
def dataset(shared_datadir):
    contents = (shared_datadir / "results_1.txt").read_text()
    return contents


def test_valid_input_content(runner, dataset):
    expected = ('1.  Tarantulas, 6 pts\n2.  Lions, 4 pts\n3.  FC Awesome, 3 pts\n4.  Snakes, 1 pts\n5.  Great, '
                '0 pts\n5.  Grouches, 0 pts\n')
    with runner.isolated_filesystem():
        with open('in.txt', 'w') as f:
            f.write(dataset)
        result = runner.invoke(cli.main, ["in.txt"])
    assert result.output == expected, "log table failed to be generated"
    assert result.exit_code == 0, "program should exit without errors"


def test_invalid_input_content(runner):
    with runner.isolated_filesystem():
        with open('in.txt', 'w') as f:
            f.write("Invalid data:, 2.0")
        result = runner.invoke(cli.main, ["in.txt"])
    assert result.output == "", "log table should be without entries"
    assert result.exit_code == 0, "program should exit without errors"


def test_basic_commands(runner):
    """Test the CLI."""
    result = runner.invoke(cli.main)
    assert result.exit_code == 2, "should exit with error, as the fixture_file argument is needed"
    assert "Error: Missing argument 'FIXTURE_FILE'" in result.output

    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0, "should print help and exit."
    assert '--help  Show this message and exit.' in help_result.output
