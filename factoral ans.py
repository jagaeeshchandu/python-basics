n=int(input("enter the number"))
f=1
while n>=1:
    if n>1:
        print(n, end = 'x')
    else:
        print(n, end = '=')
    f=f*n
    n -= 1
print(f)
    
    
