a,b,c=map(int,input().split())
s=2*a*b*c*512
s=s//1024
s=str(s)
s=s+'KB'
print(s)