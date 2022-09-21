n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))

m=[]
s=[]
for i in l1:
    if i not in s:
        s.append(i)

for i in s:
    if i in l2:
        m.append(i)
print(*m)