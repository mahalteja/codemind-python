a=input()
s='aeiouAEIOU'
b=[]
for i in a:
    if i in s and i not in b:
        b.append(i)
if len(b)>0:
    print(*b)
else:
    print(-1)