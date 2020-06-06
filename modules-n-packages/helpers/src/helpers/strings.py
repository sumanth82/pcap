# Modules are just files
# helpers.py
# Gets a phrase and returns the strings which are uppercase and lowercase vice-versa


def extract_upper(phrase):

    """
    extract_upper takes a string and returns a list containing only the 
    uppercase characters from the string 

    >>>extract_upper("Hello There, BOB")
    ['H', 'T', 'B', 'O', '']

    """
    return list(filter(str.isupper, phrase))

# The above format is called a DOCTEST ( doctest ). More like automated tests to test the function and validate the function 

#def extract_upper(phrase):
#    return list(filter(str.isupper, phrase))


def extract_lower(phrase):
    return list(filter(str.islower, phrase))


print("Hello from HELPERS")



