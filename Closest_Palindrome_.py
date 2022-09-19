def rev(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
def fow(n):
    if n==rev(n):
        n=n-1
    while n!=rev(n):
        n-=1
    return n
def bac(n):
    if n==rev(n):
        n=n+1
    while n!=rev(n):
        n+=1
    return n
a=int(input())
x=fow(a)
y=bac(a)
if abs(x-a)<abs(y-a):
    print(x)
elif abs(y-a)<abs(x-a):
    print(y)
else:
    print(x,y)