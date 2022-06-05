def dig(n):
    d=0
    if n<0:
        n=-n
    if n==0:
        return 1
    while n>0:
        d=d+1
        n=n//10
    return d
n,m=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i in l:
    if dig(i)==m:
        s=s+1
print(s)