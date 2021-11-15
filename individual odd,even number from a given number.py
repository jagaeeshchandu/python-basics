n=int(input())
s=0
e=0
w=0
o=0
while n:
    r=n%10
    if r%2==0:
        e=e*10+r
    else:
        o=o*10+r
    n=n//10
while e:
    r=e%10
    s=s*10+r
    e=e//10
print(s)
while o:
    r=o%10
    w=w*10+r
    o=o//10
print(w)

    
    

