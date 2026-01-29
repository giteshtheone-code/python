n=int(input("Enter a number in octal:"))
c=0
s=0
while n!=0:
        r=n%10
        s=s+r*(8**c)
        n//=10
        c+=1
print("Decimal number is:",s)