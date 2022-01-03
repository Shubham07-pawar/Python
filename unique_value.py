#  Write a Python program to print all unique values in a dictionary.
# [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}\

d = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
s = set()

for i in d:
    d1 = list(i.values())
    s.update(d1)
print("Unique Values:", s)


s = set(val for i in d for val in i.values())
print("Unique Values:", s)



