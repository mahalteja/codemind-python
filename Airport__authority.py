v=[]
for _ in range(int(input())):
    a=int(input())
    v.append(a)
k=int(input())
a=0
for i in v:
    if i<=k:
        a+=1
    else:
        a+=2
print(a)