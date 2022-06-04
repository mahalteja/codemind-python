n=int(input())
l=list(map(int,input().split()))
s=set(l)
m=0
for i in s:
    if i%2==0:
        m+=i
print(m)