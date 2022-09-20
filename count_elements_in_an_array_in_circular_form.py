a=int(input())
l=list(map(int,input().split()))
l.insert(0,l[-1])
l.append(l[1])
s=0
for i in range(1,a+1):
    if (l[i-1]%2==0 and l[i+1]%2!=0) or (l[i-1]%2!=0 and l[i+1]%2==0):
        s=s+1
print(s)        
