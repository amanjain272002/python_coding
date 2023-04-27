# dct = {}
# inp = input()
# for i in inp:
#     if dct.get(i) == None:
#         dct[i] = 1
#     else:
#         dct[i] = dct[i]  + 1
# print(dct)

lst = ["a","e","i","o","u","A","E","I","O","U"]
inp = input()
atr = ""
index = 0
k = 0

for i in range(0,len(inp)):
    if(lst.count(inp[i]) == 1):
        k = k+1
        if (k==1):
            index = i
    elif(lst.count(inp[i]) == 0 and k>1):
        for j in range(index,index+k):
            atr = atr + inp[j]
        k = 0
    elif(lst.count(inp[i]) == 0 and k==1):
        k=0

if(k>1):
    for j in range(index,index+k):
        atr = atr + inp[j]

print(atr)

    
