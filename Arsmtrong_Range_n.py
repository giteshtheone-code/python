lr=int(input("enter a number"))
ur=int(input("enter a number"))
c=0
s=0
t=lr
while lr<=ur:
    while lr!=0:
        lr=lr//10
        c+=1
    lr=t
    while lr!=0:
        r=lr%10
        s=s+r**c
        lr=lr//10
    lr+=1

if t==s:
    print("Armstrong number")
else:
    print("Not an armstrong number")
