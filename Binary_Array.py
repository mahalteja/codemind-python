n=int(input())
l=list(map(int,input().split()))
s=[i for i in l if i==0 or i==1]
print(s==l)