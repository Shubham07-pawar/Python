a = [0, 1, 3, 0, 12, 45, 0, 0]
s = []
r = 0
for i in range(len(a)):

    if i == 0:
        a.append(a[i])
    else:
        a.insert(r, a[i])
        r += 1

print(a)


