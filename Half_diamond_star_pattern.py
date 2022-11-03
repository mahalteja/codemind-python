n=int(input())
if n>2 and n<101:
    for i in range(1,(2*n)):
        if i<=n:
            for j in range(1,i+1):
                print('*',end='')
            print()
        else:
            for j in range(i,(2*n)):
                print('*',end='')
            print()
else:
    print('The pattern is not possible')
