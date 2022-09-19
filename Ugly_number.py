a=int(input())
s=[2,3,5]
m=0
for i in range(1,a+1):
    if a%i==0:
        if i in s or a==1:
            m=1
            print("Ugly Number")
            break
                
if m==0:
    print('Not Ugly Number')