lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
lst1 = []
lst.sort();
for i in range(1,len(lst)):
    if lst[i-1] == lst[i]:
        if lst[i] not in lst1:
            lst1.append(lst[i])


print(lst1)
    
