===================
Span Football League
===================


.. image:: https://img.shields.io/pypi/v/span_football_league.svg
        :target: https://pypi.python.org/pypi/span_football_league

.. image:: https://readthedocs.org/projects/span-footbal-league/badge/?version=latest
        :target: https://span-footbal-league.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


A command-line application that will calculate the ranking table for a league.


* Free software: Apache Software License 2.0
* Documentation (Coming Soon): https://span-football-league.readthedocs.io.

Background
--------

**The Problem**

We want you to create a production ready, maintainable, testable command-line application that
will calculate the ranking table for a league.

**Input/output**

The input and output will be text. Either using stdin/stdout or taking filenames on the command
line is fine.
The input contains results of games, one per line. See “Sample input” for details.
The output should be ordered from most to least points, following the format specified in
“Expected output”.

**The rules**

In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A loss is worth 0 points.
If two or more teams have the same number of points, they should have the same rank and be
printed in alphabetical order (as in the tie for 3rd place in the sample data).

Features
--------

* Create a League Result table/list
* Allocate points accordingly based on set rules
* Establish a Winner, Looser and manage DRAW

Installation
--------

**Requirements:** Python3, conda

Install:

.. code-block::

    $ git clone https://github.com/zipho/football_league_exercise
    $ cd marsrover
    $ conda create --name <envname> --file requirements_dev.txt
    $ conda activate <envname>


Quickstart
--------

.. code-block::

    $ python3 app/cli.py tests/data/results_1.txt

    $ python3 -m pytest tests/


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
