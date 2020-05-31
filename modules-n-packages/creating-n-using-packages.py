# Packages allows us to bundle up our modules to be utilized by others
# Package is just a dir that includes a __init__.py file

# Name of the file to identify for as a package -- __init__.py

# In this example, it's under - helpers/__init__.py file

# This is where we can put initialization code for our package 
# i.e within __init__.py file
# You can specify to use the modules from within this package ONLY!! 

__all__ = ['extract_upper']

from .strings import * 





