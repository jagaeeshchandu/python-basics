n1=int(input())
n2=int(input())
i=0
while n1<=n2:
    while n1:
        if n1%2==0:
            n1=n1//2
        else:
            n1=3*n1+1
        i+=1
        print(n1,end=" ")
print('\n',i)

   
