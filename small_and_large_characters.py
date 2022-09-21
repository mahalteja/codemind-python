a=input().split()
s=[]
for i in a:
    s.append(min(i))
    s.append(max(i))
print(*s)