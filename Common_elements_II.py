def sort(n):
    s=[]
    for i in n:
        if i not in s:
            s.append(i)
    return s
n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1=sort(l1)
l2=sort(l2)
m=[]
for i in l1:
    if i not in l2:
        m.append(i)
for i in l2:
    if i not in l1:
        m.append(i)
print(*m)