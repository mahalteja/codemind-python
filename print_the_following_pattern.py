n=int(input())
l=[str(i) for i in range(1,n+1)]
for i in range(n):
    print(''.join(l))
    l.pop()