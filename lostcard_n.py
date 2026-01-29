n=int(input())#n=5
s=0
s_n=0
for i in range(1,n):#1 2 3 4
    k=int(input())#k=1 2 3 4
    s=s+k#s=1 s=1+2=3 s=6 s=6+4=10
    s_n=s_n+i#s_n=1 s_n=1+2=3 s_n=3+3=6 s_n=6+4=10
s_n=s_n+n#s_n=10+5=15
print(s_n-s)#15-10=5