# Write a Python function that takes two lists and returns True if they have at least one common member
l1 = [10, 20, 30, 40, 50, 60]
l2 = [10, 25, 45, 55]
for i in l1:
    for x in l2:
        if i == x:
            print("TRUE")
