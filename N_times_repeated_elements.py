n=int(input())
l=list(map(int,input().split()))[:n]
a=int(input())
k=[]
for i in l:
    if l.count(i)==a:
        k.append(i)
if len(k)>0:
    print(*set(k))
else:
    print(-1)