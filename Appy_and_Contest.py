for i in range(int(input())):
    n,a,b,k=map(int,input().split())
    s=0
    for i in range(1,n+1):
        if k==s:
            break
        if i%a==0 and i%b!=0:
            s+=1
        elif i%b==0 and i%a!=0:
            s+=1
    if s>=k:
        print('Win')
    else:
        print('Lose')