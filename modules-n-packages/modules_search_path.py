# To know where the impoerts are coming from.
# https://docs.python.org/3/library/

# Example:

# import helpers
# PYTHONPATH
# PYTHONPATH = '/user/test' python3.7
# import sys    ## This is from the standard library

import sys
print(sys.path)


###### O/P ####

#$ python3
#Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
#[Clang 6.0 (clang-600.0.57)] on darwin
#Type "help", "copyright", "credits" or "license" for more information.
#>>> import sys
#>>> sys.path
#['', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/Library/Frameworks/Python.framework/Versions/3.7/lib/pyth
#on3.7/lib-dynload', '/Users/sumantrenukarya/Library/Python/3.7/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages']
#>>> 


# /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages --> This is where the 3rd party packages installed for this version of Python goes





