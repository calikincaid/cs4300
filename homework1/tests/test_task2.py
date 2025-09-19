'''
 Author: Chad Gulczynski
 Course: CS4200
 Date: 9/19/25

 TASK 2 TEST:
    Sets up a pytest test case that verifies the output of task2.py.
'''

import pytest
from src import task2

def test_task2_int_output():
    int_sum = task2.integer_add(5, 5) # run task2 integer_add to get the sum of 5 + 5
    assert int_sum == 10 # 5 + 5 should = 10

def test_task2_float_output():
    float_sum = task2.floating_add(5.5, 4.5) # run task2 floating_add to get the sum of 4.5 + 5.5
    assert float_sum == 10.0 # 4.5 + 5.5 should = 10.0

def test_task2_string_output():
    greeting = task2.string_greeting("Chad") # run task2 string_greeting to get a string that says "Welcome to task 2, Chad"
    assert greeting == "Welcome to task 2, Chad" # the greeting should equal "Welcome to task 2, Chad"

def test_task2_boolean_output():
    boolean_1 = task2.greater_than(4,5) # run task2 greater_than to get the bool output of 4 > 5
    boolean_2 = task2.greater_than(5,4) # run task2 greater_than to get the bool output of 5 > 4
    assert boolean_1 == False # 4 > 5 should be False
    assert boolean_2 == True  # 5 > 4 should be True

