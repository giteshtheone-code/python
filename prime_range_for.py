n1=int(input("Enter a number"))
n2=int(input("Enter a number"))

for i in range(n1,n2+1): #i=1 i=2
      c=0
      for j in range(1,i+1): #j=1 j=2
                  if(i%j==0):
                        c=c+1
      if(c==2):
            print(i)    
                  