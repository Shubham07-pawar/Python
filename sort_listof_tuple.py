# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given \
# list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def last(n):
    return n[-1]


def sort_1(tuples):
    return sorted(tuples, key=last)


list_1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_1(list_1))

# using lambda function
l1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l2 = sorted(l1, key=lambda x: float(x[-1]))
print(l2)
