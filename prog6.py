n = int(input("Enter number "))
count  = len(str(n))
q = n
sum=0
while n>0:
    r =n%10
    sum  =sum+r**count
    n= n//10

if sum == q:
    print("yes armstrong ")
else:
    print("no armstrong ")


