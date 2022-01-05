s = ['BBc_xyz ', ' PQR_STU', 'xyz_TSTU', ' abed_gfd ', 'bhg']
l = []
for i in s:
    a = i.replace(" ", "")
    s1 = a.find("_")
    if s1 != -1:
        l.append(a[s1 + 1:])
print(l)
