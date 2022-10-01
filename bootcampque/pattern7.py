for outer in range(1,6):
    k = outer+1
    for inner in range(1,6):
        
        if(inner<=outer):
            print(outer,end=' ')
        else:
            print(k,end=' ')
            k = k+1
    print("\n")
