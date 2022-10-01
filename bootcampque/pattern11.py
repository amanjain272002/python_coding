k = 6
for outer in range(0,12):
    if outer < 6:
        for inner in range(0,outer+1):
            print("*",end='')
        print("\n")
    else:
        for inner in range(0,k):
            print("*",end='')
            
        k =k-1
        print("\n")
