h,m=map(int,input().split(':'))
if h>12:
    h=h-12
if h==10 and m==0:
    print(0)
else:
    h=0.5 * (h * 60 + m)
    m=m*6
    angle=abs(h-m)
    print(min(360-angle,angle))