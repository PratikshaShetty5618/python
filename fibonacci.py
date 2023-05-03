# Problem Statement:
## To calculate Fibonacci Series up to n numbers.
num = int(input("Enter number: "))
while num < 0:
    print("Only positive numbers are allowed!!")
    num = int(input("Enter number: "))
# Solution 1: Using simple iteration
print("\nSolution 1: ")
res = []
n1,n2 = 0,1
res.append(n1)
res.append(n2)
for i in range(2,num+1):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    res.append(n3)
print("Fibonacci Series: ", res)

# Solution 2: Using Recursion
print("\nSolution 2:")
res = []
def find_fibonacci(n):
    if n==0 or n==1:
        return n
    return find_fibonacci(n-2) + find_fibonacci(n-1)
for i in range(0,num+1):
    res.append(find_fibonacci(i))
print("Fibonacci Series: ", res)

# Solution 3: Using Formula: Fn = {[(√5 + 1)/2] ^ n} / √5
print("\nSolution 3:")
res = []
import math
phi = (math.sqrt(5)+1)/2
for i in range(0,num+1):
    res.append(round(math.pow(phi,i)/math.sqrt(5)))
print("Fibonacci Series: ", res)
