lr=int(input("Enter a number"))
ur=int(input("Enter a number"))
s=0
if lr<ur:
    while lr<=ur:
        s=s+lr
        lr=lr+1
    print("Sum is:",s)
else:
    while ur<=lr:
        s=s+ur
        ur=ur+1
    print("Sum is :",s)