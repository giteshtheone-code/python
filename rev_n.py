n=int(input("Enter a number"))
rev=0
t=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print("Reverse of the number",t,"is",rev)