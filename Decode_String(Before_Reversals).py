for i in range(int(input())):
    m,n=map(int,input().split())
    l=input()
    for i in range(n,0,-1):
        s1=l[:i]
        l=s1[::-1]+l[i:]
    print(l)