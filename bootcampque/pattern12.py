k = int(9/2)
for outer in range(0,9):
    if outer < k+1:
        for inner in range(0,outer+1):
            print("*",end='')
        print("\n")
    else:
        for inner in range(0,k):
            print("*",end='')
        k = k-1
        print("\n")


