# Problem Statement:
## To find out whether the given Number is Palindrome or not.

num = int(input("Enter Number: "))
# Solution 1: Using Simple Iteration
print("\nSolution 1:")
reverse = 0
temp = num
while temp>0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if reverse == num:
    print("Palindrome")
else:
    print("Not Palindrome")

# Solution 2: Using Recursion
print("\nSolution 2:")
def reverse_num(num,reverse = 0):
    if num<=0:
        return reverse
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    return reverse_num(num//10,reverse)
if reverse_num(num)==num:
    print("Palindrome")
else:
    print("Not Palindrome")

# Solution 3: String Manipulation
print("\nSolution 3:")
if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")