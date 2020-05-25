# Lambdas and Collection functions

# Lambdas are anonymous functions that don't have names
# In-line functions 

# Lambda gets only 1 expression to be run within a function. 
# Use a lambda keyword to create a lambda expression

# Example function:

def square(num):
    return num*num

square(4)
print(square(4))  # O/P: 16

# Equivalent lambda and format:

# lambda <parameter>: <expression> 
# The return value in a lambda function is always the expression execution results 

square_lambda = lambda num: num*num

square_lambda(4)
print(square_lambda(4))  # O/P: 16



