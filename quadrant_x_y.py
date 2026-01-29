x, y = map(int, list(input("Insert the value for variable X and Y : ").split(" ")))
if x>0 and y>0:
    print("The point lies in the first quadrant")
elif x<0 and y>0:
    print("The point lies in the second quadrant")
elif x<0 and y<0:
    print("The point lies in the third quadrant")
elif x>0 and y<0:
    print("The point lies in the fourth quadrant")
elif x==0 and y!=0:
    print("The point lies on an axis")
elif y==0 and x!=0:
    print("The point lies on an axis")
else:
    print("The point lies at the origin")
