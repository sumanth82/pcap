# The way you set the Python interpreter using - SHEBANG:

#!/usr/bin env python 

# This creates a symlink in ~/.pyenv/versions/3.7.6/bin/python 

## Import the module using the name of the module file - import helpers 
# Modules are just files

print("We're importing 'helpers' from main")

# from <package_name>.<module_name>
from helpers.strings import *

print("We're importing 'extras' from 'main'")
from helpers import variables

name = "Sumant Renukarya"

# The way you use the module created earlier - helpers.py is {<module_name>.<function_name-in-that-module-OR-a-named-entity-in-that-module(like a var name)>}
# Example: helpers.extract_upper 
# 

import helpers

print(f"LowerCase Letters: {extract_lower(variables.name)}")  # O/P: LowerCqase Letters: ['u', 'm', 'a', 'n', 't', 'e', 'n', 'u', 'k', 'a', 'r', 'y', 'a']
print(f"Uppsercase letters: {extract_upper(variables.name)}") # O/P: Uppercase letters: ['S', 'R']
print(f"From helpers: {helpers.strings.extract_lower(variables.name)}")

# O/P: 
#sumants-mbp:modules-n-packages sumantrenukarya$ python3 main.py 
#We're importing 'helpers' from main
#Hello from HELPERS
#We're importing 'extras' from 'main'
#Importing 'helpers' in 'extras'
#LowerCase Letters: ['u', 'm', 'a', 'n', 't', 'e', 'n', 'u', 'k', 'a', 'r', 'y', 'a']
#Uppsercase letters: ['S', 'R']

##############NOTES:############

# Once the module is imported once and READ, it will NOT be read again if called, in the same module/script. 
# Hence, you have 'Hello from HELPERS' only in line 23 and not seen again after line 24
#
# What if we want to run the print statement only when running that module as a script and NOT everytime we import helpers.py as a module? 

# __name__ # is a variable - it's there always in every module; Lets us know the name of the module in a given context




