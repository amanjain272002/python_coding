ans = 1
save = 0
counter = 1
for outer in range(1,5):
    save = save + counter
    ans = save
    for inner in range(1,outer + 1):
        print(ans," ",end='')
        ans = ans - 1
    print()
    counter = counter + 1 