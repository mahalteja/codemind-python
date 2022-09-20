n=int(input())
l=[int(i) for i in input().split()]
f=0
if len(l)>3:
    for i in range(n-2):
        if l[(i)]+l[(i+1)]!=l[i+2]:
             print('no')
             break
    else:
       print('yes')
else:
    print('no')
    