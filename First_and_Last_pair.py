n=int(input())
l=list(map(int,input().split()))[:n]
if len(l)%2!=0:
    a=(len(l)//2)+1
    l.insert(a,0)
s=[]
while len(l)>0:
    s.append(l[0])
    s.append(l[-1])
    l.pop(-1)
    l.pop(0)
print(*s)