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
n=int(input())
l=list(map(int,input().split()))[:n]
for i in l:
    print(dig(i),end=' ')
