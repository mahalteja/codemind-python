n=int(input())
l=list(map(int,input().split()))[:n]
s=[i for i in l if i%2==0]
print(len(l)==len(s))