# Different ways to clear a list in Python
# l1 = [10, 24, 10, 45, 40, 74]
# l1.clear()
# print(l1)

# 2nd way
l1 = [10, 24, 10, 45, 40, 74]
l1 = []
print(l1)

# 3rd way
l1 = [10, 24, 10, 45, 40, 74]
l1 *= 0
print(l1)

# 4th way
l1 = [10, 24, 10, 45, 40, 74]
del l1[:]
print(l1)
