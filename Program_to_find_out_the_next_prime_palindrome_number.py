def rev(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
def prime(n):
    fc=0
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                fc+=1
    return(fc==0)
def fow(n):
    n=n+1
    while rev(n)!=n:
        n=n+1
    return n
a=int(input())
while prime(fow(a))!=True:
    a=fow(a)
print(fow(a))