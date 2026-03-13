# And so it begins..

# Uh, what do I need?
# secure way to generator truly random characters
# ask how long the password should be?
# maybe complex -> ask what special characters that need to be used 
# ask what special characters you can't use? 
# store [terrible advice in real life, but you know, it's a intro project fam] 
#   passwords, e.g. remember the last 10 passwords. 

# maybe for later -> password protect this generator 
# still not secure for sure 

import secrets
import string



lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
safe_symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?'

# Verify if input is an int first, idk it works
while True:
    password_length = input("How long do you want your password? ")
    try: 
        value = int(password_length)
        if value <= 0:
            print(f"Passwords can't be negative or zero length!")
        elif value > 30:
            print(f"Keep it between 1 and 30 characters!")
        else:    
            print(f"The input '{password_length}' is a valid integer.")
            break
    except ValueError:
        print(f"Invalid input! Try again!")
# Ask user what they want 
password_pool = ""
letters_check = input("Do you want letters in your password? Type Y for Yes, or N for No: ")
if letters_check == 'Y':
    password_pool += lowercase + uppercase
print(password_pool)

numbers_check = input("Do you want numbers in your password? Type Y for Yes, or N for No: ")
if numbers_check == 'Y':
    password_pool += numbers
print(password_pool)

symbols_check = input("Do you want symbols in your password? Type Y for Yes, or N for No: ")
if symbols_check == 'Y':
    password_pool += safe_symbols
print(password_pool)

pool_length = len(password_pool)
generated_password = ""

count = 0 
while count < value:
    random_int = secrets.randbelow(pool_length)
    generated_password += password_pool[random_int]
    count += 1
print(generated_password)

# CURRENTLY CLAPPED OUT CODE, WILL FIX LATER LMAO