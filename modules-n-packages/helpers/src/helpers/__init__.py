
# Docstrings to document the package
# It's a string and not a comment 
# THe module will have a __doc module that we can access later 

# When you import the package, you can use the <module/package_name>.__doc__ to get the details on the package 


"""

Helpers is a package that provides easy to use helper functions

"""



# Package is 
# Name of the file to identiy for as a package -- __init__.py

# This is where we can put initialization code for our package 
# i.e within __init__.py file
# You can specify to use the modules from within this package ONLY!! 

__all__ = ['extract_upper']

from .strings import * 


