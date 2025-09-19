'''
 Author: Chad Gulczynski
 Course: CS4200
 Date: 9/19/25

 TASK 4 TEST:
    Sets up a pytest test case that verifies the input and output of task4.py
'''

import pytest
from src import task4

# ---- TESTING INPUTS: Check the result of inputting non numeric, 0, and negative values for the percentage ----

# Sticker price tests section
def test_task4_sticker_price_negative(capsys):
    task4.calculate_discount(-50, 50) # run task 4 calculate_discount with negative sticker price
    captured = capsys.readouterr()  # captures stdout/stderr
    assert captured.out == "invalid sticker price value input\n" # tests if the stdout text is the same as what we want it to be

def test_task4_sticker_price_string(capsys):
    task4.calculate_discount("fifty", 50) # run task 4 calculate_discount with string sticker price
    captured = capsys.readouterr()  # captures stdout/stderr
    assert captured.out == "invalid sticker price value input\n" # tests if the stdout text is the same as what we want it to be

def test_task4_sticker_price_zero(capsys):
    task4.calculate_discount(0, 50) # run task 4 calculate_discount with 0 sticker price
    captured = capsys.readouterr()  # captures stdout/stderr
    assert captured.out == "invalid sticker price value input\n" # tests if the stdout text is the same as what we want it to be

# Discount percentage tests section
def test_task4_percentage_negative(capsys):
    task4.calculate_discount(50, -50) # run task 4 calculate_discount with negative sticker price
    captured = capsys.readouterr()  # captures stdout/stderr
    assert captured.out == "invalid percentage value input\n" # tests if the stdout text is the same as what we want it to be

def test_task4_percentage_string(capsys):
    task4.calculate_discount(50, "fifty") # run task 4 calculate_discount with string sticker price
    captured = capsys.readouterr()  # captures stdout/stderr
    assert captured.out == "invalid percentage value input\n" # tests if the stdout text is the same as what we want it to be

def test_task4_percentage_zero(capsys):
    task4.calculate_discount(50, 0) # run task 4 calculate_discount with string sticker price
    captured = capsys.readouterr()  # captures stdout/stderr
    assert captured.out == "invalid percentage value input\n" # tests if the stdout text is the same as what we want it to be

# ---- TESTING OUTPUTS: Check the results of task 4 calulate_discount ----
def test_task4_calculate_discount():
    discount_price_1 = task4.calculate_discount(5, .5) # testing with int sticker price and float percentage
    discount_price_2 = task4.calculate_discount(5, 50) # testing with int sticker price and int percentage
    discount_price_3 = task4.calculate_discount(.5, .5) # testing with float sticker price and float percentage
    discount_price_4 = task4.calculate_discount(50, 10.5) # testing with float sticker price and float value above 1

    assert discount_price_1 == 2.5
    assert discount_price_2 == 2.5
    assert discount_price_3 == .25
    assert discount_price_4 == 44.75
