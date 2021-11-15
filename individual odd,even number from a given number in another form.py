n=int(input())
s=0
e=0
w=0
o=0
while n:
    r=n%10
    s=s*10+r
    n=n//10
print(s)
while s:
    r=s%10
    if r%2==0:
        e=e*10+r
    else:
        o=o*10+r
    s=s//10
print(e)
print(o)

    

