'''
 Author: Chad Gulczynski
 Course: CS4200
 Date: 9/19/25

 TASK 5 TEST:
    Sets up a pytest test case that verifies the output of subtasks 1 and 2 in task5.py
'''

import pytest
from src import task5

# ---- TESTING SUBTASK 1: Create a list of your favorite books, including book titles and authors ----
def test_task5_book_list(capsys):
    favorite_books = task5.book_list() # assign the list of books to favorite_books variable
    captured = capsys.readouterr()  # captures stdout/stderr
    assert captured.out == "[['The Republic', 'Plato'], ['Politics', 'Aristotle'], ['Leviathan', 'Thomas Hobbes']]\n" # tests if the stdout text is the same as what we want it to be    
    
    assert isinstance(favorite_books, list) # ensure that the book list is a list data type
    
    length = len(favorite_books) # gets the length of the list so we can loop through it
    for i in range(length): 
        assert isinstance(favorite_books[i], list) # ensure that the book list indices are all also a list data type

# ---- TESTING SUBTASK 2: Create a dictionary that represents a basic student database, including student names and their corresponding student IDs ----
def test_task5_student_database():
    students = task5.student_database() # assign the dictionary of students to students variable

    assert isinstance(students, dict) # ensure that the students dictionary is a dictionary data type
    
    # Ensure that each student id is mapped to the correct student
    assert students[1] == "Abe"
    assert students[2] == "Brian"
    assert students[3] == "Chad"
    assert students[4] == "Dave"

