# Syntax error causes the file never to run at all
# Exceptions occur during run time 
#E.g:

print("Hello world")

#'a

# O/P:  File "exception-handling.py", line 6
#    'a
#     ^
#SyntaxError: EOL while scanning string literal

## EXCEPTION Example:

print(1 + 'a')

# O/P, which is an exception: ( Seen when the line is executed or after it is executed)

#Traceback (most recent call last):
#  File "exception-handling.py", line 16, in <module>
#    print(1 + 'a')
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

