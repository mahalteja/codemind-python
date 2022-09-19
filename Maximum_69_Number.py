a=b=int(input())
s=list(str(a))
for i in range(len(s)):
    if s[i]=='6':
        s[i]='9'
        break
    else:
        i+=1
print(''.join(s))