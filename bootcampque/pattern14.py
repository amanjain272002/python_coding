k = int(10/2)
for outer in range(0,10):
    if outer < 5:
        for inner in range(0,outer+1):
            print(end=" ")
        for inner in range(outer,5):
            print('* ',end='')
    
        print("\n")
    else:
        for inner in range(outer ,10):
            print(end=" ")
        for inner in range(k,outer+1):
            print('* ',end='')
        
        print("\n")
