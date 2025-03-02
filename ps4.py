
#Write a program to display the multiplication table of a given number. First 20
num1 = 8
for i in range (1, 21):
  print(num1, '*', i, '=', num1 * i)


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Input number
number = int(input("Enter a number to calculate its factorial: "))

# Check if the number is negative
if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {number} is {factorial(number)}.")


#Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
