l=list(input().split())
v='AEIOUaeiou'
m=0
for i in l:
    i=list(i)
    if len(i)%2!=0:
        i.insert((len(i)//2)+1,' ')
    while len(i)>0:
        if (i[0] in v and i[-1] not in v) or (i[0] not in v and i[-1] in v):
            m=m+1
        i.pop(0)
        i.pop(-1)
print(m)