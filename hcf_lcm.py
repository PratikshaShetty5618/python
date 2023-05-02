# Problem Statement
## Take 2 numbers as inputs and find their HCF and LCM.

num1,num2 = int(input("Enter 1st Number: ")), int(input("Enter 2nd Number: "))
#Solution 1: Linear Quest
print("\nSolution 1: ")
## LCM:
# For a input num1 and num2. This method uses two following observations –
# 1. LCM of two numbers will at least be equal or greater than max(num1, num2)
# 2. Largest possibility of LCM will be num1 * num2
lcm = num1*num2
for i in range(max(num2,num2),(num1*num2)+1):
    if i%num1==0 and i%num2==0:
        lcm = i
        break
print("LCM: ",lcm)
## HCF:
# 1. Initialize HCF = 1
# 2. Run a loop in the iteration of (i) between [1, min(num1, num2)]
# 3. Note down the highest number that divides both num1 & num2
# 4. If i satisfies (num1 % i == 0 and num2 % i == 0) then new value of HCF is i
# 5. Print value of HCF
hcf = 1
for i in range(1,min(num1,num2)+1):
    if num1%i==0 and num2%i==0:
        hcf = i
print("HCF: ",hcf)

# Solution 2: Repeated subtraction for HCF and addition for LCM
print("\nSolution 2: ")
## LCM:
# Rather than linearly checking for LCM by doing i++. We can do i = i + max
lcm = num1*num2
for i in range(max(num1,num2),(num1*num2)+1,max(num1,num2)):
    if i%num1==0 and i%num2==0:
        lcm = i
        break
print("LCM: ",lcm)
# Rather than incrementing by 1, we will decrement with min(num1,num2)
n1,n2 = num1,num2
while n1!=n2:
    if n1>n2:
        n1-=n2
    else:
        n2-=n1
print("HCF: ", n1)

# Solution 3: HCF can be improvised with recursion and LCM can be calculated with HCF
print("\n Solution 3: ")
def find_hcf(n1,n2):
    if n1==0 or n2==0: #Everything divides 0
        return n1+n2
    elif n1==n2: #Actual Base Condition
        return n1
    #Recursion Stmt
    elif n1>n2:
        return find_hcf(n1-n2,n2)
    else:
        return find_hcf(n1,n2-n1)
hcf = find_hcf(num1,num2)
print("LCM: ",(num1*num2)//hcf) # Formula: product of 2 nos = hcf * lcm
print("HCF: ",hcf)

# Solution 4: Using Euclidean algorithm to find HCF
print("\nSolution 4: ")
# 1. If b is equals to 0 return a
# 2. Else recursively call the function for value b, a%b and return
def find_hcf(n1,n2):
    return n2==0 and n1 or find_hcf(n2,n1%n2)
hcf = find_hcf(num1,num2)
print("LCM: ",(num1*num2)//hcf) # Formula: product of 2 nos = hcf * lcm
print("HCF: ",hcf)








