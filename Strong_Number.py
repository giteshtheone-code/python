n=int(input("Enter a number"))
t=n
s=0
while n>0:
    r=n%10
    i=1
    f=1
    while i<=r:
        f=f*i
        i+=1
    s=s+f
    n=n//10
n=t
if n==s:
    print(n,"is a strong number")
else:
    print(n,"is not a strong number")