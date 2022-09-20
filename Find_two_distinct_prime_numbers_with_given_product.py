def prime(n):
    fc=0
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            fc+=1
    return (fc==0)
a=int(input())
v=[]
for i in range(1,a+1):
    if a%i==0:
        if i!=a//i and prime(i)==True and prime(a//i)==True:
            print(i,a//i)
            break
else:
    print('-1')
