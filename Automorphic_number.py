n=int(input("Enter a number"))
r1=n%10
s=r1*r1
r2=s%10

if r2==r1:
    print(n,"is an automorphic number")
else:
    print(n,"is not an automorphic number")       