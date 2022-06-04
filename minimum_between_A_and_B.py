n=int(input())
l=list(map(int,input().split()))[:n]
a,b=map(int,input().split())
s=[]
for i in l:
    if i>=a and i<=b :
        s.append(i)
if len(s)>0:
    print(min(s))
else:
    print(-1)