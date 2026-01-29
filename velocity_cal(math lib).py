import math
a=int(input("enter acceleration"))
u=int(input("Enter initial velocity"))
s=int(input("Enter distance"))

v=math.sqrt(u*u+2*a*s)
print("Final velocity:",v)
           