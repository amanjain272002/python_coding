for outer in range(1,6):
    for inner in range(1,11-outer):
        if inner<outer:
            print(" ",end='')
        elif(outer%2==0) and (inner%2==0):
            print("*",end='')
        elif (outer%2==0) and (inner%2!=0):
            print(" ",end='')
        elif(outer%2!=0) and (inner%2!=0):
            print("*",end='')
        elif (outer%2!=0) and (inner%2==0):
            print(" ",end='')
       
    print()


for outer in range(5,0,-1):
    for inner in range(1,11-outer):
        if inner<outer:
            print(" ",end='')
        elif(outer%2==0) and (inner%2==0):
            print("*",end='')
        elif (outer%2==0) and (inner%2!=0):
            print(" ",end='')
        elif(outer%2!=0) and (inner%2!=0):
            print("*",end='')
        elif (outer%2!=0) and (inner%2==0):
            print(" ",end='')
       
    print()
