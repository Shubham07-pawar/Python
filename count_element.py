# Count occurrences of an element in a list

l1 = [1, 2, 4, 8, 8, 7, 6, 2, 1, 4, 8, 7, 6, 1, 2, 2, 1, 4, 5, 6, 7]
print(l1.count(2))

c = 0
for i in l1:
    if i == 2:
        c += 1
print(c)
