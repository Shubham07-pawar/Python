# sort the list using first digit/unit
# if first digit/unit is same then check next digit/unit.
l1 = [43, 35, 45, 67, 138]
l2 = sorted(l1, key=lambda x: [int(j) for j in str(x)], reverse=True)
print(l2)

