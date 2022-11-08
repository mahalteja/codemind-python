a=int(input())
b=list(map(int,input().split()))
c=b[:(a//2)-1:-1]
d=b[:a//2]
print(*(c+d),sep=' ')