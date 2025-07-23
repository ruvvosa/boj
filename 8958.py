count = int(input())

for i in range(count):
    num = 0
    total =0
    a = list(input())
    for j in a:
        if j == 'O':
            num += 1
            total += num
        else:
            num = 0
    print(total)
        
    
            
