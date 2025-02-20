#i. Write a program to check if a given number is positive,negative, or zero.
num1 = float(input("enter a number: "));
if num1 > 0:
  print("positive number");
elif num1>=0:
  print("zero");
else:
  print("negative number")

#2.Determine if a number is odd or even.
x = 25;
if x % 2== 0:
  print("even number");
else:
  print("odd number")

#Check if a person is eligible to vote (age >= 18)
age = 65
if age >= 18:
  print("yes, you are eligible for voting");
else:
  print("oh No! you are not eligible for voting");

#Write a program to find the greatest of two numbers.
num1 = 25;
num2 = 25;
if num1>num2:
  print("num1")
elif num1<num2:
  print("num2")
else:
  print("both numbers are equal")

#Print "Pass" if a student scores more than 40 marks; otherwise, print "Fail."
score = 40;
if score > 40:
  print("pass");
elif score<40:
  print("fail");
else:
  print("equal")

#Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.).
day_number = 7
if day_number == 1:
  print("monday");
elif day_number == 2:
  print("tuesday");
elif day_number == 3:
  print("wednesday");
elif day_number == 4:
  print("thursday");
elif day_number == 5:
  print("friday");
elif day_number == 6:
  print("saturday");
else:
  print("sunday");

#Implement a simple calculator to perform addition, subtraction, multiplication, and division.
operation= ( '+', '-', '*',' /' )
num1= 98
num2= 35
if operation == 'add' or operation== ' + ' :  #if operation in ['add','+']
  print(num1+num2)
elif operation == 'mul'or operation==' * ':
  print(num1*num2)
elif operation == 'div'or operation== ' / ':
  if num2 ==0:
    print("division not possible")
  else:
    print(num1/num2)
elif operation == 'sub' or operation== ' - ':
   print(num1-num2)
else:
  print("invalid")


#Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.).
month_number = 13
if month_number == 1:
  print("janurary");
elif month_number == 2:
  print("february");
elif month_number == 3:
  print("march");
elif month_number == 4:
  print("april");
elif month_number == 5:
  print("may");
elif month_number == 6:
  print("june");
elif month_number == 7:
  print("july");
elif month_number == 8:
  print("august");
elif month_number == 9:
  print("septmember");
elif month_number == 10:
  print("october");
elif month_number == 11:
  print("november");
elif month_number == 12:
  print("decmember");
else:
  print("invalid");


#Write a program to find the greatest of three numbers.
num1 = 35;
num2 = 46;
num3 = 58;
if num1 > num2 and num1 > num3:
  print("num1");
elif num1 >= num2 and num1 >= num3:
  print("num1=num2=num3");
elif num2 > num1 and num2 > num3:
  print("num2")
else:
  print("num3")

#Check if a year is a leap year
leap_year = 2000;
if leap_year % 4 == 0:
  print(" leap year");
else:
  print(" not a leap year")

#Write a program to classify a character entered by the user as a vowel, consonant, or neither.
char = input('enter a single character')
if len(char) not in [1]:  #length of character !=1
  print("invalid")
else:
  if char in['a', 'e', 'i', 'o', 'u']:
    print("vowels")
  elif char .isalpha():
    print("consonants")
  else:
    print("other or special characters")
  
# Calculate the grade of a student based on the marks they
#score:
#1. 90-100: Grade A
#2. 80-89: Grade B
#3. 70-79: Grade C
#4. <70: Fail.
calculate_grade = float(input("enter marks:  " ))
if 100> calculate_grade > 90 :
  print( "grade A" );
elif 89 >  calculate_grade > 80:
  print(" grade B ");
elif 79 >  calculate_grade > 70:
  print( "  grade C ");
else:
  print("fail");


#Write a program to check if three sides length form a valid triangle.
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
if a+b> c  and a+c> b and b+c > a:
  print(" traingle formed")
else:
  print("not traingle formed")

