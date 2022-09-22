a=list(input().lower())
b=list(input().lower())
a.sort()
b.sort()
if len(a)==len(b) and a==b:
    print(True)
else:
    print (False)