n=int(input())
l=list(map(int,input().split()))[:n]
k=[]
s=0
for i in l:
    if l.count(i)==i and i not in k:
        s+=1
        k.append(i)
if len(k)>0:
    print('%.2f'%(sum(k)/len(k)))
else:
    print(-1)