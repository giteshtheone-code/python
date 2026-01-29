n=int(input("Enter a number"))
i=2
f=1
while i<=n:
    if n%i==0:
        t=n//i
        f=f*i
        n=t
    else:
        i+=1
    print(i)