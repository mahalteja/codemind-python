a=list(input())
m=0
for i in a:
    if a.count(i)==1 and (i.lower() not in a or i.upper()not in a):
        m=m+1
print(m)
