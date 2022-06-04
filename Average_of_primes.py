def prime(n):
    f=0
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            f==1
            return False
            break
    if f==0:
        return True
n=int(input())
l=list(map(int,input().split()))
s=m=0
for i in l:
    if prime(i)==True:
        s=s+i
        m=m+1
print('%.2f'%(s/m))