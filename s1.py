# s = [(1, 2, 3, 4), (4, 2, 1, 3), (5, 6, 2, 1), (2, 5, 2, 1)]
# s1 = []
# for i in range(0, 4):
#     s2 = s[0][i] + s[1][i] + s[2][i] + s[3][i]
#     s1.append(s2)
# print(tuple(s1))
# --------------------------------------------------------------------------------------------------------------------
# input: 14, 625, 498.002
# op: 14.625.498, 002
# i = 14, 625, 498.002
# s = str(i).replace(" ", "")
# s1 = s.replace(",", "-").replace(".", ", ").replace("-", ".")
# print(s1[1:16])
'''
s = 'aaabbbsaaaakkdkjdddd'
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
print(d)
'''