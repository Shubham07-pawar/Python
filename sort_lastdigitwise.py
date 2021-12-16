# sort the list using last digit/unit
# if last digit/unit is same then check next digit/unit.
l1 = [43, 35, 45, 67, 138]
l2 = sorted(l1, key=lambda x: str(x)[-1])
print(l2)
