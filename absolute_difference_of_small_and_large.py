a=input().split()
s=[]
for i in a:
    s.append(abs(ord(max(i))-ord(min(i))))
print(*s)