# There is a way to hide certain entities within a module from being shown/exposed when imported in another module
# Example: 
# from helpers_1 import *
# 
# In such way of importing a module, we can use a method in helpers_1.py to restrict what is exposed in the helpers module
# USE:
# __all__ = ['extract_upper'] # list of strings that indicate the vars/functions that needs to be exposed


# Alternatively, when you define a function/variable in a module which starts with _ , it is be default hidden
# Example:

# def _extract_upper():


