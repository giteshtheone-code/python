s=input("Enter a string")
l=len(s)
rs=s[:(l+1)//2]
ls=s[(l+1)//2:]
print(ls+rs)