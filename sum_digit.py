#  Sum of number digits in List
# using for loop
"""
l1 = [10, 24, 54, 84, 78, 96, 45, 32, 12]
l2 = []
for i in l1:
    sum = 0
    for j in str(i):
        sum += int(j)
    l2.append(sum)
print(l2)
------------------------------------------------------------------------------------------------------------------------

# lambda function
l1 = [10, 24, 54, 84, 78, 96, 45, 32, 12]
s = list(map(lambda x: sum(int(y) for y in str(x)), l1))
print(s)
------------------------------------------------------------------------------------------------------------------------
"""
# list comprehension with lambda function
from functools import reduce as rd

l1 = [10, 24, 54, 84, 78, 96, 45, 32, 12]
l2 = [rd(lambda x, y: int(x) + int(y), list(str(i))) for i in l1]
print(l2)


