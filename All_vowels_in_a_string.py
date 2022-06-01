a=input()
s='aeiou'
e=[]
for i in a:
    if i in s and i not in e:
        e.append(i)
print(len(e)==len(s))