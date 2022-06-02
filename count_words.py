a=input()
b=a.split(' ')
s='aeiouAEIOU'
q=0
for i in b:
    if i[0] in s and i[len(i)-1] not in s:
        q+=1
print(q)