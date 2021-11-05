n=int(input("enter the number"))
i=1
while(i<=n):
    if i%3==0:
        i += 1
        continue
    print(i,end=" ")
    i += 1
    
