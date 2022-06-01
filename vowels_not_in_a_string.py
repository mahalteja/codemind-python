a=input()
s='aeiou'
b=[]
for i in s:
    if i not in a and i not in b:
        b.append(i)
if len(b)>0:
    print(*b)
else:
    print(0)