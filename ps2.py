#Print all numbers from 1 to 100 using a for loop.
for i in range (1, 101):
  print(i);

sum = 0
for i in range(1, 101):
  print(i)
  sum =  sum+i #sum += i
print(sum)


#Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)
n = 10
print((n*(n+1))/2)

#Print all even numbers between 1 and 50 using a while loop.
num1 =1
while num1 <= 50:
  print(num1)
  num1 +=1


#Write a program to display the multiplication table of a given number. First 20
num1 = int(input("enter the number: "));
for i in range(1, 21):
  print(num1, '*', i, '=', num1*i)
for i in range(1, 9):
    print(num1, '*', i, '=', num1*i );

#Reverse a number using a while loop.
#1. Also can we get the sum of all the digits

num1 = 256389
# number to string  and again string to number
num1 =  56723
# q = 5672,   r = 3
#q = 567, r= 2 3*10+2 = 32
#q = 56, r= 7  32*10+7= 327
#q = 5 r = 6 327*10+6 =3276
#q = 0,  r= 5  3276*10+5 32765
rev_num = 0
while num1 > 0:
   rem = num1 %10
   rev_num = rev_num *10+ rem
   num1 = num1// 10
print(rev_num)

num2 = 10235698
rev_num1 = 0
digit_sum = 0
while num2 > 0:
   rem1 = num2 % 10
   digit_sum += rem1
   rev_num1 = rev_num1 *10+rem1
   num2 = num2 //10
print(rev_num1)
print(digit_sum)


#Write a program to count the number of digits in a given number using a while loop.
num1 =  1586947632105624
count = 0
while num1 > 0:
   num1 = num1//10
   count +=1
print(count)
num1 += 1

# you sholud never tamper with the inputs
if rev_num1 == num2:
   print("palindrome")
else:
   print("not a palindrome")

#Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a while loop.

db_username = 'virat_kohil'
db_password = '51_centuries'


total_rem_chances = 3
while total_rem_chances > 0:
   input_username = input("enter a username")
input_password = input(" enter password")
if input_username == db_username  and input_password == db_password :
   print("login successful")
else:
   total_rem_chances -=1
   print("invalid credintals")
   print("you still have", total_rem_chances, "chances")
   

   













