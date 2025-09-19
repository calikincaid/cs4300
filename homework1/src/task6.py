'''
 Author: Chad Gulczynski
 Course: CS4200
 Date: 9/19/25

 TASK 5:
    Read task6_read_me.txt and count the number of words in it
'''

def word_count(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        words = text.split() # split words by whitespace into a list
        return len(words)

def task6_words():
    filename = "/home/student/cs4300/homework1/task6_read_me.txt"
    words = word_count(filename)
    print(words)

def main():
    task6_words()

if __name__ == "__main__":
    main()