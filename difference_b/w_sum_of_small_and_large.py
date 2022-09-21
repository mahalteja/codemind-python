a=input().split()
mi=0
ma=0
for i in a:
    mi=mi+(ord(min(i)))
    ma=ma+(ord(max(i)))
print(abs(mi-ma))