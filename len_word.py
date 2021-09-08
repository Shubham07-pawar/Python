#  Write a Python program to find the list of words that are longer than n from a given list of words
"""
# using for loop
s = "python is nice programming language"
l1 = s.split()
n = 3
l2 = []
for i in l1:
    if len(i) > n:
        l2.append(i)
print(l2)
------------------------------------------------------------------------------------------------------------------------

# while loop
s = "python is nice programming language"
l1 =  s.split()
l2 = []
n = 3
s1 = 0
while s1 < len(l1):
    if len(l1[s1]) > n:
        l2.append(l1[s1])
    s1 += 1
print(l2)
------------------------------------------------------------------------------------------------------------------------

# using list comprehension
s = "python is nice programming language"
print([x for x in s.split() if len(x) > 3])
------------------------------------------------------------------------------------------------------------------------
"""







