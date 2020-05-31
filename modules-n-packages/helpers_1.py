# There is a way to hide certain entities within a module from being shown/exposed when imported in another module
# Example: 
# from helpers_1 import *
# 
# In such way of importing a module, we can use a method in helpers_1.py to restrict what is exposed in the helpers module
# USE:

# __all__ = ['extract_upper'] # list of strings that indicate the vars/functions that needs to be exposed


__all__ = ['extract_upper']

def extract_upper(phrase):
    return list(filter(str.isupper, phrase))


def extract_lower(phrase):
    return list(filter(str.islower, phrase))


# print("Hello from HELPERS") # Prints this when this module is imported in another module and run. If you want to make this optional? 
# run below: 

if __name__ == "__main__":
    print("Hello from HELPERS")

# O/P:

#python3 helpers_1.py 
# Hello from HELPERS

# To un as just a module:
# $ python3 -m helpers_1
# Hello from HELPERS

