a=(input().lower()).split()
b=(input().lower()).split()
s=[]
for i in b:
    if i in a and i not in s:
        s.append(i)
print(*s)