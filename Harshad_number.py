n=int(input("Enter a number"))
s=0
t=n
while n>0:
    r=n%10
    s=s+r
    n=n//10
if t%s==0:
    print("It's a Harshad number")
else:
    print("It's not a Harshad number")
