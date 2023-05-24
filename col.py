p = open("col.txt",'r')
char = 0
l = 0
wc = 0
# print(p.read())
for line in p:
    for k in range(0,len(line)): 
        char +=1
        if(line[k]==' '): 
            wc+=1
        if(line[k]=='\n'):
            wc+=1 
            l+=1

print(char,l+1,wc+1)
p.close()