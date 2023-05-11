lst = [{'sname' : 'aman','sage' : 18,'marks' : [10,20,30]},{'sname' : 'aditya','sage' : 18,'marks' : [100,200,300]}]
dct = {'cal':  lambda x:sum(x)//len(x)}

# for i in lst:
#     print(i['marks'])
s = []
# print(dct['cal'](lst[0]['marks']))
# print(dct['cal'](lst[1]['marks']))

for i in range(0,len(lst)):
    s.append(dct['cal'](lst[i]['marks']))
print(dct['cal'](s))

