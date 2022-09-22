def pal(n):
    s=list(n)
    s.reverse()
    s=''.join(s)
    return(s==n)
    
a=(input().lower()).split()
m=0
for i in a:
    if pal(i)==True:
        m=m+1


print(m)