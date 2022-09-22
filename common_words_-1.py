a=(input().lower()).split()
b=(input().lower()).split()
s=[]
for i in a:
    if i in b and i not in s:
        s.append(i)
print(len(s))