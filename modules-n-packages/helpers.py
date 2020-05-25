# helpers.py
# Gets a phrase and returns the strings which are uppercase and lowercase vice-versa

def extract_upper(phrase):
    return list(filter(str.isupper, phrase))


def extract_lower(phrase):
    return list(filter(str.islower, phrase))


print("Hello from HELPERS")



