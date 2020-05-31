from helpers_1 import *
import extras_1

print(f"__name__ in main_1.py is: {__name__}")

# __name__ # is a variable - it's there always in every module; Lets us know the name of the module in a given context


print(f"Uppercase letters: {extract_upper(extras_1.name)}")
print(f"Lowercase letters: {extract_lower(extras_1.name)}")

# O/P:

# python3 main_1.py 
# Hello from HELPERS
# __name__ in helpers_1.py is: helpers_1
# __name__ in extras_1.py is: extras_1
# __name__ in main_1.py is: __main__
# Lowercase letters: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']
# Uppercase letters: ['K', 'T']


