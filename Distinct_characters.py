a=list(input())
m=[]
for i in a:
    if i.lower() not in m and i!=' ':
        m.append(i.lower())
m.sort()
print(''.join(m))