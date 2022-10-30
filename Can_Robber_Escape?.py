n=int(input())
l=list(map(int,input().split()))
odd=0
for i in range(n):
    if l[i]%2!=0:
        odd+=1
if odd<=2:
    print('YES')
else:
    print('NO')