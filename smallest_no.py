#  Write a Python program to get the smallest number from a list
"""
d1 = [10, 20, 45, 41, 21, 32, 12]
print(min(d1))
------------------------------------------------------------------------------------------------------------------------

# using built in method
d1 = [10, 20, 45, 41, 21, 32, 12]
d1.sort()  # d1.sort(reverse= True)
print(d1[0]) # print(d1[-1])
------------------------------------------------------------------------------------------------------------------------

# using while loop
d1 = [10, 2, 45, 41, 21, 32, 12]
s = d1[0]
r = 0
while r < len(d1):
    if s > d1[r]:
        s = d1[r]
    r += 1
print(s)
------------------------------------------------------------------------------------------------------------------------

# using for loop
d1 = [10, 2, 45, 41, 21, 32, 12]
s = d1[0]
for i in d1:
    if i < s:
        s = i
print(s)
------------------------------------------------------------------------------------------------------------------------



# using function

def minimum(d):
    s = d[0]
    for i in d:
        if i < s:
            s = i
    return print(s)


d1 = [10, 2, 45, 41, 21, 32, 12]
minimum(d1)
------------------------------------------------------------------------------------------------------------------------
"""





