_=int(input())
a=list(map(int,input().split()))
s=''
for i in a:
    s+=str(i)
s=int(s)
s+=1
for i in str(s):
    print(i,end=' ')