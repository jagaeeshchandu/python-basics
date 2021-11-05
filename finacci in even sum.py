n=int(input("enter the number"))
a=0
b=1
c=a+b
sum=0
while(c<n):
    c=a+b
    a=b
    b=c
    if(c%2==0):
        sum=sum+c      
print(sum)

