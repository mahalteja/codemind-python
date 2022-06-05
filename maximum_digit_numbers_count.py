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
l=list(map(int,input().split()))
s=[]
for i in l:
    s.append(dig(i))
for i in l:
    if dig(i)==max(s):
        print(i,end=' ')