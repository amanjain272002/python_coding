for outer in range(1,9):
    for inner in range(1,9):
        if inner <= outer:
            print(inner*outer,end=' ')
    print("\n")