n=int(input())
l=list(map(int,input().split()))
s=0
m=[]
for i in range(len(l)):
    if i%2!=0 and l[i]%2!=0:
        s=s+1
for i in l:
    if i%2!=0:
        m.append(i)
print(s>=len(m))