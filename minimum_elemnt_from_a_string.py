a=input().split()
a=a[len(a)-1]
s=min(a)
if chr(ord(s)+32) in a:
    print(chr(ord(s)+32))
else:
    print(s)