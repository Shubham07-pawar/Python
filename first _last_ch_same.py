# Write a Python program to count the number of strings where the string length is 2 or more and the first and
# last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
"""
# using for loop
list_1 = ['abc', 'xyz', 'abxa', '1221']
for i in list_1:
    if len(i) > 1 and i[0] == i[-1]:
        print(i)
------------------------------------------------------------------------------------------------------------------------
# using while loop

list_1 = ['abc', 'xyz', 'abxa', '1221']
s = 0
while s < len(list_1):
    r = list_1[s]
    if r[0] == r[-1]:
        print(r)
    s+= 1
------------------------------------ ------------------------------------------------------------------------------------



# using function

def fun1(d):
    for i in d:
        if i[0] == i[-1]:
            print(i)


list_1 = ['abc', 'xyz', 'abxa', '1221']
fun1(list_1)
------------------------------------------------------------------------------------------------------------------------
"""





