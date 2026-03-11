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

lowercase_length = len(lowercase)
secure_int = secrets.randbelow(lowercase_length)
print(lowercase[secure_int])
