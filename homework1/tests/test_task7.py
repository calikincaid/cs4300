'''
 Author: Chad Gulczynski
 Course: CS4200
 Date: 9/19/25

 TASK 7 TEST:
    Sets up a pytest test case that verifies the square roots calculated by numpy in task7.py
'''

import pytest
from src import task7

def test_task7_get_square_roots():
    square_roots = task7.get_square_roots([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
    square_roots = square_roots.tolist() # we need to turn the numpy array into a normal python list to compare
    assert square_roots == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

