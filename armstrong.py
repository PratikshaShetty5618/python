# Problem Statement
## To find Armstrong Number between two given number.

# What is Armstrong Number? abcd... = a^n + b^n + c^n + d^n + ...

start = int(input("Enter Start Range: "))
end = int(input("Enter End Range: "))

# Solution 1: Using Iteration
print("\nSolution 1:")
import math
def check_armstrong(num):
    sum = 0
    length = len(str(num))
    temp = num
    while temp != 0:
        remainder = temp % 10
        sum += math.pow(remainder,length)
        temp = temp//10
    if sum == num:
        return True
    else:
        return False
res = []
for n in range(start,end+1):
    if check_armstrong(n):
        res.append(n)
print("Armstrong Numbers are: ",res)

# Solution 2: Using Recursion
print("\nSolution 2:")
import math
def sum_digits(num,sum=0,length=-1):
    if length == -1:
        length = len(str(num))
    if num==0:
        return sum
    remainder = num % 10
    sum+=math.pow(remainder,length)
    num = num//10
    return sum_digits(num,sum,length)

res = []
for n in range(start,end+1):
    if sum_digits(n)==n:
        res.append(n)
print("Armstrong Numbers are: ",res)




