a=list(input())
s=[i for i in a if a.count(i)==1]
if len(s)>0:
    print(s[0])
else:
    print(-1)