# Ways to check if element exists in list
# using if - else
"""
l1 = [10, 20, 30, "abc", "xyz"]
if "abc" in l1:
    print("present in this list")
else:
    print("Not present in this list")
------------------------------------------------------------------------------------------------------------------------

# using while loop
l1 = [10, 20, 30, "abc", "xyz"]
s = 0
while s < len(l1):
    if 100 in l1:
        print("Element exists")
    else:
        print("Element not exists")
    break
------------------------------------------------------------------------------------------------------------------------
"""
# using lambda function
l1 = [10, 20, 30, "abc", "xyz"]
s = filter(lambda x: x if 10 in x else print("d"), ["10", "20", "30", "abc", "xyz"])
print(list(s))
