def odd(n):
    return(n%2!=0)
def even(n):
    return(n%2==0)
n=int(input())
l=list(map(int,input().split()))[:n]
s=[]
while len(l)>0:
    for i in l:
        if odd(i)==True:
            s.append(i)
            l.pop(l.index(i))
            break
    for i in l:
        if even(i)==True:
            s.append(i)
            l.pop(l.index(i))
            break
if len(s)%2!=0:
    s.append(0)
print(*s)