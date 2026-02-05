def unionArray(a,b):
    s=set()
    for x in a :
        s.add(x)
    for x in b :
        s.add(x)
    return sorted(list(s))
a = [1,2,3,2,1]
b = [3,2,2,3,3,2]
print(unionArray(a,b))