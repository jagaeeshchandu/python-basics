n=int(input("enter the number"))
s=0
t=n
while n:
     r=n%10
     s=s*10+r
     n=n//10
if t==s:
     print(" palindrome")
else:
     print("not palindrome")

    
