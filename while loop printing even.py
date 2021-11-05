n=int(input("enter the number"))
i=1
fc=0
while(i<=n):
 if(n%i==0):
    fc=fc+1
i += 1
if(fc==2):
     print("prime")
else:
    print("notprime")
