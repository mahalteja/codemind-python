n=int(input())
a=65
l=[chr(a+i) for i in range(n)]
for i in range(n):
    for j in range(n):
        print(l[i],end=' ')
    print()