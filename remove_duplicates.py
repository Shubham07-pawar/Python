# Write a Python program to remove duplicates from a list.
"""
list_1 = [10, 20, 30, 40, 30, 50, 40, 70, 20]
s = set(list_1)
print(list(s))
------------------------------------------------------------------------------------------------------------------------

# using for loop

list_1 = [10, 20, 30, 40, 30, 50, 40, 70, 20]
unique = []
for i in list_1:
    if i not in unique:
        unique.append(i)
print(unique)
------------------------------------------------------------------------------------------------------------------------

#  using while loop

list_1 = [10, 20, 30, 40, 30, 50, 40, 70, 20]
s = 0
l1 = []
while s < len(list_1):
    if list_1[s] not in l1:
        l1.append(list_1[s])
    s += 1
print(l1)
------------------------------------------------------------------------------------------------------------------------

# using lambda function
list_1 = [10, 20, 30, 40, 30, 50, 40, 70, 20]
s = set(map(lambda x:x, list_1))
print(list(s))
------------------------------------------------------------------------------------------------------------------------
"""
# using function


def duplicate(n):
    l1 = []
    for i in n:
        if i not in l1:
            l1.append(i)
    return print(l1)


list_1 = [10, 20, 30, 40, 30, 50, 40, 70, 20]
duplicate(list_1)
