a=input()
a=a.split(' ')
s='aeiou'
for i in a:
    e=[]
    for j in i:
        if j in s :
            e.append(j)
    print(len(e),end=' ')