m,n=map(int,input().split())
mat=[]
s=0
d=0
for i in range(n):
    l=list(map(int,input().split()))[:m]
    mat.append(l)
for i in range(1,m-1):
    for j in range(1,n-1):
        s+=mat[i][j]
for i in range(m):
    for j in range(n):
        d+=mat[i][j]
print(d-s)