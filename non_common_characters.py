a=list(input().lower())
b=list(input().lower())
s=[]
for i in a:
    if i not in b and i not in s and i!=' ':
        s.append(i)
for i in b:
    if i not in a and i not in s and i!=' ':
        s.append(i)
s.sort()
print(''.join(s))