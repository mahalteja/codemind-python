a=list(input().lower())
m=[]
for i in a:
    if a.count(i)==1 and i.lower() not in m and i!=' ':
        m.append(i.lower())
m.sort()
print(''.join(m))