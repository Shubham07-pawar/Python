# 1. Write a Python program to sum all the items in a list.
# using built function
"""
d = [10, 20, 45, 41, 21, 32, 12]
print(sum(d))
-----------------------------------------------------------------------------------------------------------------------

# using for loop
d = [10, 20, 45, 41, 21, 32, 12]
count = 0
for i in d:
    count += i
print(count)
------------------------------------------------------------------------------------------------------------------------

# using while loop
d = [10, 20, 45, 41, 21, 32, 12]
count = 0
r = 0

while r < len(d):
    count += d[r]
    r += 1

print(count)
------------------------------------------------------------------------------------------------------------------------
# using function recursion
def sum_1(d):
    s = 0
    for element in d:
        if type(element) == type([]):
            s = s + sum_1(element)
        else:
            s += element
    return print(s)


sum_1([10, 20, 45, 41, 21, 32, 12])
------------------------------------------------------------------------------------------------------------------------
# function recursion
def recursive_list_sum(data_list):
    total = 0
    for element in data_list:
        if type(element) == type([]):
            total = total + recursive_list_sum(element)
        else:
            total = total + element

    return total


print(recursive_list_sum([10, 20, 45, 41, 21, 32, 12]))
-----------------------------------------------------------------------------------------------------------------------

# using lambda
from functools import reduce as rd

d = [10, 20, 45, 41, 21, 32, 12]
print(rd(lambda x, y:x + y, d))
-----------------------------------------------------------------------------------------------------------------------
"""
d = [10, 20, 45, 41, 21, 32, 12]
