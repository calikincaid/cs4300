'''
 Author: Chad Gulczynski
 Course: CS4200
 Date: 9/19/25

 TASK 1 TEST:
    Sets up a pytest test case that verifies the output of task.py.
'''

import pytest
from src import task1

def test_task1_output(capsys): # capsys documentation https://docs.pytest.org/en/stable/reference/reference.html#capsys
    task1.main()  # run task1 to print "Hello, World!" to the console
    captured = capsys.readouterr()  # captures stdout/stderr
    assert captured.out == "Hello, World!\n" # tests if the stdout text is the same as what we want it to be