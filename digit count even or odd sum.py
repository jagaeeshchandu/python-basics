n=int(input("enter the number"))
i=0
r=0
d=0
while n:
    r=n%10
    if(r%2==0):
        i+=r
    else:
        d+=r
    n=n//10
print("even",i)
print("odd",d)
