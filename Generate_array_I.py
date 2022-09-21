a=int(input())
l=list(map(int,input().split()))
n=[]
s=0
for i  in range(a):
    if i%2==0:
        n.append(l[i])
    else:
        for m in range(l[i]-1):
            n.append(l[i-1])
print(*n)