n=int(input())
l=list(map(int,input().split()))
l.reverse()
s=0
for i in range(n):
    s=s+l[i]*(2**i)
print(s)