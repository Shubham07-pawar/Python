l = ["a", 'b', 'c', 'e', 'd']
s =[]
while l:
    min = l[0]
    for i in l:
        if i < min:
            min = i
    s.append(min)
    l.remove(min)
print(s)