n,m=map(int,input().split())
if n==1 and m==10 or n==10 and m==1:
    print('Yes')
elif m==n+1 or n==m+1:
    print('Yes')
else:
    print('No')
    