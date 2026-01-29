n=int(input("Enter a number in binary"))
t=n
c=0
s=0
i=0
while n>0:
    n=n//10
    c+=1
n=t
if c%3==0:
    r=n%10
    s=s+r*(2**i)
    n=n//10
    i+=1
    print("The octal equivalent is",s)
