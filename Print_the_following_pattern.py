l=[i for i in range(1,int(input())+1)]
for i in range(len(l)):
    for j in l:
        print(j,end=' ')
    print()
    l.pop(0)