'''
 Author: Chad Gulczynski
 Course: CS4200
 Date: 9/19/25

 TASK 4:
    Calculates the final price of a product after applying a given discount percentage inside of a function named calculate_discount.
        - The function should accept any numeric type for price and discount
'''

# ---- calculate_discount applies a given discount percentage ----
def calculate_discount(sticker_price, percentage):
    if isinstance(sticker_price, int) or isinstance(sticker_price, float): # if the sticker price is a float or int make sure that its greater that 0
        if sticker_price <= 0:
            print("invalid sticker price value input") # if the sticker price is not greater than 0 print error message
            return
    else:
        print("invalid sticker price value input") # if the sticker price is not a numeric data type print error message
        return
    
    if isinstance(percentage, int) or isinstance(percentage, float):
        if percentage <= 0:
            print("invalid percentage value input")
            return     
        elif percentage >= 1: # if the value is greater or equal to one, turn it into its decimal percentage equivalent
            percentage = percentage / 100.0 # dividing by float will cast result into float if the percentage was an int before
    else:
        print("invalid percentage value input")
        return

    discount = sticker_price * percentage

    return sticker_price - discount
