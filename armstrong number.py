n=int(input('enter the number'))
s=0
l=0
t=n
q=n
while n:
     l+=1
     n = n//10
print(l)
while t:
     r=t%10
     s+=r**l
     t=t//10
if(s==q):
     print('armstrong')
else:
     print('not armstrong')
