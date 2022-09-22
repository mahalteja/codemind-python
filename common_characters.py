a=list(input().lower())
b=list(input().lower())
s=[]
for i in a:
    if i in b and i not in s and i!=' ':
        s.append(i)
for i in b:
    if i in a and i not in s and i!=' ':
        s.append(i)
s.sort()
if len(s)>0:
    print(''.join(s))
else:
    print(-1)