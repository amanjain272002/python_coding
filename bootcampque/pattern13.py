k =int(9/2)
for outer in range(0,9):
    if outer < 5:
        for inner in range(outer,5):
            print(end=" ")

        for inner in range(0,outer+1):
            print("*",end='')
        print("\n")
    else:
        for inner in range(k,outer+1):
            print(end=" ")

        for inner in range(0,9-outer):
            print("*",end='')
        
        print("\n")
