'''
 Author: Chad Gulczynski
 Course: CS4200
 Date: 9/19/25

 TASK 5:
    Subtask 1: Create a list of your favorite books, including book titles and authors and print the first 3 entries.
    Subtask 2: Create a dictionary that represents a basic student database, including student names and their corresponding student IDs.
'''
# ---- SUBTASK 1: Create a list of your favorite books, including book titles and authors ----
def book_list():
    favorite_books = [
        ["The Republic", "Plato"],
        ["Politics", "Aristotle"],
        ["Leviathan", "Thomas Hobbes"],
        ["The Prince", "Niccolo Machiavelli"]
    ]

    print(favorite_books[:3]) # prints all the elements of the list before index 3 of the list
    return favorite_books

# ---- SUBTASK 2: Create a dictionary that represents a basic student database, including student names and their corresponding student IDs ----
def student_database():
    students = {
        1 : "Abe",
        2 : "Brian",
        3 : "Chad",
        4 : "Dave",
    }

    return students