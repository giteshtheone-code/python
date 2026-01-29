n=int(input("Enter a number in decimal:"))
rev=0
i=2
while(n>0):
    if n%i==0 or n%i==1:
      r1=n%2
      rev=rev*10+r1
      t=n//2
    n=t
m=rev[-1::-1]
print("Binary number is:",m)
