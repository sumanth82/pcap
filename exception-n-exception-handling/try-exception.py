# How to perform exception handling? Use try; If something goes wrong, catch the error and do something using except 
# Some of the examples for an exception errors are TypeError and Index Error 

import sys
import random

#try:
#    print(f"Received argument {sys.argv[1]}")
#except:
#    print("Error: No arguments. Please provide atleast 1")
#    sys.exit(1)

#O/P: 

#$python3.7 try-exception.py Hello
#Received argument Hello1

#$python3.7 try-exception.py 
#Error: No arguments. Please provide atleast 1



########## In the below you say, if there is an IndexError go to first except statement and pass the Error as err, else go to 2nd Except statement

try:
    print(f"Received argument {sys.argv[1]}")
    args = sys.argv
    random.shuffle(args)
    print(f"Randon Argument {args[0]}")
except IndexError as err:
    print("Error: No arguments. Please provide atleast 1 ({err})")
    sys.exit(1)
except NameError:
    print(f"Error: random module not loaded")
    sys.exit(1)
else:                                   # else is run when no exception is caught    
    print("else is running")
finally:                                # finally options runs ALWAYS
    print("Finally is running")


# O/P: 1

#$python3.7 try-exception.py 
#Error: No arguments. Please provide atleast 1 ({err})
#Finally is running

# O/P: 2 (Did not have import random line defined while running this to throw the error)

#$python3.7 try-exception.py Hello
#Received argument Hello
#Error: random module not loaded
#Finally is running

# O/P: 3

#$python3.7 try-exception.py Python
#Received argument Python
#Randon Argument try-exception.py
#else is running
#Finally is running







