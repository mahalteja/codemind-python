def square(n):
    s=0
    while n>0:
        r=n%10
        s=s+(r**2)
        n=n//10
    return s

a=int(input())

while a>9:
    a=square(a)
if a==1 or a==7:
    print(True)
else:
    print(False)
    