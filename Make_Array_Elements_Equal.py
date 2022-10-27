n=int(input())
l=list(map(int,input().split()))
if len(set(l))==1:
    print(0)
else:
    mc=c=0
    for i in range(n):
        c=0
        for j in range(i,n):
            if l[i]==l[j]:
                c+=1
                if mc<c:
                    mc=c
    
    print(mc)