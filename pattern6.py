# Print Pascal's Triangle in Python
from math import factorial

# input n
n = 7
for i in range(n):
	print()
	for j in range(i+1):
		if(i-j>=0):
		    print(factorial(i)//(factorial(j)*factorial(i-j))," ", end="")
	
	
