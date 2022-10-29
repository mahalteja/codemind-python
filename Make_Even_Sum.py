n=int(input())
l=list(map(int,input().split()))
e=[i for i in l if i%2==0]
if len(e)>=2:
    print(1)
else:
    print(0)