for outer in range(1,6):
    for inner in range(1,6):
        if(inner<=outer):
            print(outer,end='')
        else:
            print(inner,end='')
    print()