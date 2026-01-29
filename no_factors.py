n=int(input("Enter a number"))
s=0
c=0
while n!=0:
    r=n%10
    s=s+r
    c=c+1
    n=n//10
print("Sum of digits is",s)
print("Count of digits is",c)
