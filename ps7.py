#sum of odd numbers in given number
n=int(input("Enter the number : "))
s=0
while n>0:
    n1=n%10
    if(n1%2==1):
        s=s+n1
    n=n//10
print("Sum of odd numbers in given number :",s)

#find smallest digit prime in given number
def is_prime(digit):
    if digit < 2:
        return False
    for i in range(2, int(digit**0.5) + 1):
        if digit % i == 0:
            return False
    return True

def smallest_prime_digit(number):
    str_num = str(number)
    smallest_prime = None

    for digit in str_num:
        int_digit = int(digit)
        if is_prime(int_digit):
            if smallest_prime is None or int_digit < smallest_prime:
                smallest_prime = int_digit

    return smallest_prime

number = 3572
result = smallest_prime_digit(number)

if result is not None:
    print(f"The smallest prime digit in {number} is {result}")
else:
    print(f"There are no prime digits in {number}")


# armstrong number
num = 9464
temp = num
count = 0
temp2 = num
while temp2 > 0:
  count += 1
  temp2 //= 10
temp = num
sum = 0
while temp > 0:
  digit = temp % 10
  str1 =str(num)
  sum += digit ** len(str1)
  temp //= 10
if(sum == num):
  print(num, "is a armstrong number")
else:
  print(num, "is not a armstrong number")


