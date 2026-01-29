n1=int(input("Enter a number"))
n2=int(input("Enter a number"))
hcf=1
for i in range(1,min(n1,n2)): #while checking for factors first, excluding the number itself while performing gcd, so added min fun in btw two numbers  
    if n1%i==0 and n2%i==0:
        hcf=i         # storing common factor 
    i+=1
print("HCF is:",hcf)