#  find lcm

# n1 = int(input())
# n2 = int(input())
# for i in range(max(n1,n2),n1*n2+1):
#     if (i%max(n1,n2)==0 and i%min(n1,n2) == 0):
#         print(i)
#         break


#  find gcf
n1 = int(input())
n2 = int(input())
for i in range(2,min(n1,n2)+1):
    if (max(n1,n2)%i==0 and min(n1,n2)%i == 0):
        print(i)
        break