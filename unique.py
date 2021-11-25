
from collections import Counter


def singleNumber(nums):
    freq = Counter(nums)
    for i in freq:
        if freq[i] == 1:
            return i


a = [4, 4, 5, 6, 5, 1, 2, 3, 3, 2, 1]

s = singleNumber(a)
print(int(s))