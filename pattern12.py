for outer in range(1,6):
    for inner in range(1,6):
        if(inner>5-outer):
            print("*",end='')
           
    print()

for outer in range(4,0,-1):
    for inner in range(1,6):
        if(inner>5-outer):
            print("*",end='')
        
    print()