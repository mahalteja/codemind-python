a=int(input())
l=[0,1]
for i in range(3,a+1):
    v=l[i-2]+l[i-3]
    l.append(v)
print(*l)
