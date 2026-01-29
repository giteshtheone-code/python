n=int(input("enter a number"))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if n==s:
    print("It's a perfect number")
else:
    print("Not a perfect number")