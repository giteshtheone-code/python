n=int(input("Enter a number"))
c=0
i=2
while i<=n//2: #2<=3 
    if n%i==0: # 7%2==0 7%3
        c+=1   #
    i+=1  #i=3
if c==0:
    print("Prime number")
else:
    print("Not a prime number")