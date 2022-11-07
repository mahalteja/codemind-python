n=int(input())
m=1
s=' '
l=[(str(i)) for i in range(1,n+1)]
for i in range(n):
    if n!=i+1:
        print(s.rjust(n-1-i)+l[i]*m)
    else:
        print(l[i]*m)
    m+=2