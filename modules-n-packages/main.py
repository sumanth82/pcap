## Import the module using the name of the module file - import helpers 

print("We're importing 'helpers' from main")
from helpers import *

print("We're importing 'extras' from 'main'")
import extras

name = "Sumant Renukarya"

# The way you use the module created earlier - helpers.py is {<module_name>.<function_name-in-that-module-OR-a-named-entity-in-that-module(like a var name)>}

print(f"LowerCase Letters: {extract_lower(extras.name)}")  # O/P: LowerCqase Letters: ['u', 'm', 'a', 'n', 't', 'e', 'n', 'u', 'k', 'a', 'r', 'y', 'a']
print(f"Uppsercase letters: {extract_upper(extras.name)}") # O/P: Uppercase letters: ['S', 'R']


# O/P: 
#sumants-mbp:modules-n-packages sumantrenukarya$ python3 main.py 
#We're importing 'helpers' from main
#Hello from HELPERS
#We're importing 'extras' from 'main'
#Importing 'helpers' in 'extras'
#LowerCase Letters: ['u', 'm', 'a', 'n', 't', 'e', 'n', 'u', 'k', 'a', 'r', 'y', 'a']
#Uppsercase letters: ['S', 'R']



