n=(input("Enter a number in hexadecimal:"))
s=0
c=0
l=str(len(n))
i=0
for i in range(int(l)-1,-1):
    r=n%10
    if r>= 'A' and r<='F':
        r=ord(r)-55
    s=s+r*(16**c)
    n=n//10
    c+=1
else:
    s=s+r*(16**c)

    

    
print("Decimal number is:",s)#C90