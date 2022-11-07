n=int(input())
l=[i for i in range(n,0,-1)]
for k in range(n):
    for i in l:
        print(i,end=' ')
    print()    