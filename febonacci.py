n=int(input("Enter a number"))
i1=0
i2=1
print(i1,i2,end=' ')

for i in range(2,n):
    i3=i1+i2
    i1=i2
    i2=i3
    print(i3, end=' ')
