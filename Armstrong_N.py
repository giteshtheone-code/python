n=int(input("enter a number"))
c=0
s=0
t=n
while n>0: #371
    n=n//10 #
    c+=1#c=3
n=t
while n>0:
    r=n%10
    s=s+r**c
    n=n//10
if t==s:
    print(t ,"is an Armstong Number")
else:
    print("Not an Armstrong Number")
