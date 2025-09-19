'''
 Author: Chad Gulczynski
 Course: CS4200
 Date: 9/19/25

 TASK 6 TEST:
    Sets up a pytest test case that verifies the word count output of task6.py
'''

import pytest
from src import task6

def test_task6_word_count(capsys):
    task6.task6_words() # run the task6_words function to print the word count of the task6_read_me.txt file
    captured = capsys.readouterr() # captures stdout/stderr
    assert captured.out == "104\n" # tests if the stdout text is the same as what we want it to be
