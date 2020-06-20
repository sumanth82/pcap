# map(), filter(), zip() and reduce() functions:

def multiply_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by_2([1, 2, 3]))  # O/P [2, 4 6]


#### map(<function>, <iterable>)

# So the equivalent of the above function will be:

def test_func(item):
    return item*2

map(test_func, [1,2,3])

print(map(test_func, [1,2,3]))              # O/P: <map object at 0x10443c110> 
print(list(map(test_func, [1,2,3])))        # O/P: [2, 4, 6]

##### filter(<func name>, <list>)  ##########
## Based on the boolean value returned from a function, filter will either try to keep the returned item in the list or not 

my_list = [1,2,3]

def only_odd(item):
    return item % 2 !=0 # This means it's a odd number; This tells its an odd number 

filter(only_odd, my_list)

print(filter(only_odd, my_list))            # O/P: <filter object at 0x100e6e2d0>
print(list(filter(only_odd, my_list)))      # O/P: [1, 3]


######### zip(<string_a>, <string_b>) OR zip(<list_a>, <list_b>) OR zip(<iterable_1>, <iterable_2>) OR zip(<list_a>, <tuple_b>)

my_list = [1,2,3]
your_list = [10,20,30]

zip(my_list, your_list)
print(zip(my_list, your_list))              # <zip object at 0x106daac30>
print(list(zip(my_list, your_list)))        # O/P; [(1, 10), (2, 20), (3, 30)]

########### reduce() #################
# To use - from functools import reduce 
# reduce (<function>, <sequence_or_list>, <initial_accumulator(by_default= 0)>)
# Take a list and combine all the values in a list to a single accumulated value 

from functools import reduce

my_list = [ 1,2,3 ]

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))

# O/P: 0 1
#1 2
#3 3
#6














