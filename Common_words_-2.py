a=(input().lower()).split()
b=(input().lower()).split()
s=[]
for i in a:
    if i in b and i not in s and a.count(i)==1 and b.count(i)==1:
        s.append(i)
print(len(s))