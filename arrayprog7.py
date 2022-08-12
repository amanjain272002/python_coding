def monotic(lst):
     return (all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or
            all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1)))

lst  =[1,2,3,4,5,6]
print(monotic(lst))