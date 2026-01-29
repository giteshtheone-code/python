n=int(input("Enter binary number: "))
c=-1
s=0
i=1
while n!=0:
    d=n%10
    n=n//10
    c=c+1
    s=s+(d*(2**c))
print("Decimal number is:",s)