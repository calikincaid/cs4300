'''
 Author: Chad Gulczynski
 Course: CS4200
 Date: 9/19/25

 TASK 3:
    Subtask 1: Check if a value is positive, negative, or zero
    Subtask 2: Print the first 10 prime values
    Subtask 3: Use a while loop to calculate the sum of 1-100
'''
# ---- SUBTASK 1: Check if a value is positive, negative, or zero ----
def sign_check(value):
    if isinstance(value, int) or isinstance(value, float):

        if value == 0:
            return "zero" # if the value equals zero return zero

        elif value > 0:
            return "positive" # if the value is greater than zero return positive

        elif value < 0:
            return "negative" # if the value is less than zero return negative

    else:
        return "invalid input" # if the value is none of the above the user didnt enter in a numeric value

# ---- SUBTASK 2: Print the first 10 prime values ----
def is_prime(value):
    if value <= 1: # primes start with 2, so anything less than 2 is not prime
        return False

    else:
        for i in range(2, value): # for loop checks all values starting with two up to the value - 1
            if value % i == 0: # if the value is divisible by any of the numbers between 2 and value - 1, it is not prime
                return False
        return True

def first_10_primes():
    for i in range(30): # checks up to 29 because 29 is the 10th prime
        prime = is_prime(i) # for every value of i check if its prime or not
        if prime == True: # if the value is prime then print it to the console
            print(i)

# ---- SUBTASK 3: Use a while loop to calculate the sum of 1-100 ----
def sum_1_to_100():
    current_value = 1 # we want to begin with the value one
    total = 0

    while(current_value < 101): # while loop continues up to the current value equaling 100 and then is done
        total += current_value # add the current value to the total and store the new total
        current_value += 1 # increment the current value by one

    print(total) # print out the total sum after the while loop is completed


