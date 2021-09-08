# Swap elements in String list (swap string character is contains in list)
# replace method
l1 = ["abc", "xyz", "python", "function"]
print(l1)
l2 = [swap.replace("a", "x").replace("x", "a").replace("c", "f") for swap in l1]
print(l2)

# using join(),replace(), split()
l1 = ["abc", "xyz", "python", "function"]
l2 = ",".join(l1)
print(l2)
l3 = l2.replace("a", "y").replace("y", "f").replace("t", "T").split(",")
print(l3)

