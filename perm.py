n=int(input("Enter number"))
r=int(input("enter number"))
n1=1
r1=1
for i in range(1,n+1):
    n1=n1*i
for j in range(1,(n-r)+1):
    r1=r1*j
perm=n1//r1
print("The permutation is",perm)
