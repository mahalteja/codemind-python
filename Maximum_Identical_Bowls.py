n=int(input())
l=list(map(int,input().split()))
for i in range(n,0,-1):
    if sum(l)/i==sum(l)//i:
        print(i)
        break