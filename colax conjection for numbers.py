a = int(input())
b = int(input())
max_steps = 0
max_number = 0
while a <= b:
    current_steps = 0
    d = a
    while d>1:
        if d%2==0:
            d = d//2
        else:
            d = 3*d+1
        current_steps += 1
    if current_steps > max_steps:
        max_steps = current_steps
        max_number = a
    a += 1
print('Number:', max_number)
print('Steps:', max_steps)
    
