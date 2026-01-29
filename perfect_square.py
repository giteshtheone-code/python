import math
n=int(input("enter a number"))       
s=math.sqrt(n)
if s*s==n:
    print(n,"is a perfect square")
else:
    print(n,"is not a perfect square")