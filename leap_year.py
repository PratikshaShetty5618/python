# Problem Statement:
## Input a year and find whether it is a leap year or not.

# Solution:
## Any year that is evenly divisible by 4 is a leap year: for example, 1988, 1992, and 1996 are leap years.
## However, there is still a small error that must be accounted for. To eliminate this error, the Gregorian calendar stipulates that
## a year that is evenly divisible by 100 (for example, 1900) is a leap year only if it is also evenly divisible by 400.

## To determine whether a year is a leap year, follow these steps:
## 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
## 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
## 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
## 4. The year is a leap year (it has 366 days).
## 5. The year is not a leap year (it has 365 days).

year = int(input("Year: "))

## Solution 1: Same as the steps mentioned above
print("Solution 1:", end=" ")
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year!")
        else:
            print("Not a Leap year!")
    else:
        print("Leap year!")
else:
    print("Not a leap year!")

## Solution 2: Combined steps in single if statement
print("Solution 2:", end=" ")
if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
    print("Leap Year!")
else:
    print("Not a Leap Year!")
