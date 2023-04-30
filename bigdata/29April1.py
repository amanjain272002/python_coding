#   que 2
# inp = input()
# st = set()
# lt = []
# start = 0
# for i in range(0, len(inp)):
#     if inp[i] == " ":
#         lt.append(inp[start:i])
#         start = i+1
# print(lt)
# for i in lt:
#     st.add(i)
# print(st)

# strt = " "
# for i in st:
#     strt = strt + i
# print(strt)

# que 3
inp = input()
a = b = c = d = 0
if (len(inp) < 6 and len(inp) > 15):
    print("NO ")
else:
    for i in inp:
        if i >= 'A' and i <= 'Z':
            a = 1
        elif i >= 'a' and i <= 'z':
            b = 1
        elif i >= '0' and i <= '9':
            c = 1
        elif i == '@' or i == '#' or i == '!' or i == '$':
            d = 1

if(a == 1 and b == 1 and c == 1 and d == 1):
    print("YES")
else:
    print("NO")