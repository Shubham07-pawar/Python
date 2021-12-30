# wap to print k number of maximum values
# do not change the original list.
l = [1, 2, 3, 4, 5, 6, 8, 4, 1, 20]
k = 3
l1 = []
s = max(l)
while len(l1) != k:
    for i in l:
        if i == s and l1.count(s) == 0:
            l1.append(i)
    s -= 1
print(l1)



 