lr=int(input("Enter a number"))
ur=int(input("Enter a number"))
c=0
while lr<=ur:
    i=2
    flag=1
    while i*i<=lr:
        if lr%i==0:
            flag=0
            break
        i=i+1
    if flag==1:
        print(lr) 
    lr+=1
   