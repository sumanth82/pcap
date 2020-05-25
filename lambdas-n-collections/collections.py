# from functools import reduce

# Higher order functions that are used as parameters in functions 

#### map - map a function over a collection #####

# f(x) = 1+x

#Here, we have:

#Domain (value fed to x): [1, 2]
#Range (output of f(x)): [2, 3] 

# map() takes 2 things; It takes function as 1st argument ; 2nd thing is collection it's working over 
# map(<function>, <domain-or-collection>)

domain = [1,2,3,4,5] # This acts like an iterator or a collection

# let's say the function is f(x) = x*2

our_range=map(lambda num: num*2, domain)
print(list(our_range)) # O/P: [2, 4, 6, 8, 10]


#### filter() - If the expression is true returns the lambda expression value as a list ######

evens = filter(lambda num:num % 2 == 0, domain)
print(list(evens)) # O/P: [2, 4]


##### reduce() - lets us take an iterable, modifying the accumulator - Needs functools module to be imported
# Usage - sum of items in a list
# Here lambda takes 2 values - acc, <domain>
# acc = accumulator 

# the_sum = reduce(lambda acc, num: acc + num, domain, 0) # 0 = used for the initial value of num

# O/P: 15

##### sorted() - Will create a new list altogether  #############

Words = ['Boss', 'sum', 'a', 'cde']
print('Sort the above words')
print(sorted(Words)) # O/P: ['Boss', 'a', 'cde', 'sum']


print('sorting with a lambda key')
print(sorted(Words, key=lambda s: s.lower())) # O/P: ['a', 'Boss', 'cde', 'sum']

## sort method will just change the list 
print('sorting with a method')
Words.sort(key=str.lower, reverse = True)  # O/P: ['sum', 'cde', 'Boss', 'a']
print(Words)

#####  













