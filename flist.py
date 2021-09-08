"""#Iterate through every number in a list to separate out even and odd numbers. Identify possible outlier values as well.
a = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
even = []
odd = []
outlier = []
for i in a:
    if i > 90:
        outlier.append(i)
    elif i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"the even number is {even}")
print(f"the odd number is {odd}")
print(f"the outlier number is {outlier}")
# Find the sum of all numbers in a list.....

#Calculate the sum of even numbers in a list...
a = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
s = 0
for i in a:
    if i % 2 == 0:
        s += i
print("The sum of even numbers in the list", s)
#Count the number of even numbers in a list.....
a = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
#count = []
#for i in a:
#    if i % 2 == 0:
#        count.append(i)
#print(len(count))
#another approch
count = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        count += 1
print(count)
#Calculate the cumulative sum of all elements in a list....
a = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
s = 0
b = []
for i in a:
    s += i
    b.append(s)
print("cumulative sum of the list",b)
#Loop through two different lists and aggregate them with zip function....
a = [1,2,3,4,5]
b =['wadhe','dipak','sandip','rahul']
for i,j in zip(a,b):
    print(i,j)
-----------------------------------------------------------------------------
"""

# wap to find greater number using lambda function





