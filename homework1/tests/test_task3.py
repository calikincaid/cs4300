'''
 Author: Chad Gulczynski
 Course: CS4200
 Date: 9/19/25

 TASK 3 TEST:
    Sets up a pytest test case that verifies the output of subtasks 1, 2, and 3 in task3.py
'''

import pytest
from src import task3

# ---- TESTING SUBTASK 1: Check if a given number is positive, negative, or zero ----
def test_task3_sign_check():
    sign_value_0 = task3.sign_check(0)
    sign_value_1 = task3.sign_check(5)
    sign_value_2 = task3.sign_check(-5)
    sign_value_3 = task3.sign_check(-5.7)
    sign_value_4 = task3.sign_check("one")

    assert sign_value_0 == "zero" # 0 input should output "zero"
    assert sign_value_1 == "positive" # postive input should output "positive"
    assert sign_value_2 == "negative" # negative input should output "negative"
    assert sign_value_3 == "negative" # negative input should output "negative"
    assert sign_value_4 == "invalid input" # non numeric values should output "invalid input"

# ---- TESTING SUBTASK 2: Print the first 10 prime values ----
def test_task3_first_10_primes(capsys):
    task3.first_10_primes() # run task 3 first_10_primes function to print the first 10 primes to the console
    captured = capsys.readouterr()  # captures stdout/stderr
    assert captured.out == "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n" # tests if the stdout text is the same as what we want it to be

# ---- TESTING SUBTASK 3: Print the sum of values 1-100 ----
def test_task3_sum_1_to_100(capsys):
    task3.sum_1_to_100() # run task 3 sum_1_to_100 function to print the sum of values 1-100
    captured = capsys.readouterr()  # captures stdout/stderr
    assert captured.out == "5050\n" # tests if the stdout text is the same as what we want it to be

