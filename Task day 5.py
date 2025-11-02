print("variables of different data types")
a=int(input("Enter a integer:"))
b=float(input("Enter a decimal number: "))
c=str(input("Enter a string:"))
d=bool(input("Enter a boolean"))
e=list(input("Enter a list:"))
print(a,"is a",type(a))
print(b,"is a",type(b))
print(c,"is a",type(c))
print(d,"is a",type(d))
print(e,"is a",type(e))
print()
print("sentence using variables")
name=input("Enter your name:")
age=int(input("Enter your age:"))
print("My name is " ,name,"and My age is  :",age)
print()
print("Sum,Difference,Product,Quotient")
num1=int(input("Enter a number1"))
num2=int(input("Enter a number2"))
print("Addition:",num1+num2)
print("Subtraction:",num1-num2)
print("Product:",num1*num2)
print("Quotient:",num1/num2)
print()
print("String and Integer properly using f-string")
name=input("Enter your name:")
age=int(input("Enter your age:"))
print(f"My name is {name},and My age is  :,{age}")
print()
print("Arithmetic operators")
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
Avg=(a+b+c)/3
print("Square of a number:",a**2)
print("Cube of a number:",b**3)
print("Average of three numbers:",Avg)
print()
print("Relational opreators")
a=int(input("Enter a number"))
b=int(input("Enter a number"))
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print()
print("Logical oprators")
a=int(input("Enter a number"))
b=int(input("Enter a number"))
if a>0 and a%2==0:
    print("The number is positive and even:" ,a)
elif a<0 or a==0:
    print("The number is negative or zero:",b)
else:
    print("The number is odd")
print()    
print("Swap two variables ")
a=int(input("Enter a number"))
b=int(input("Enter a number"))
a,b=b,a
print(a,b)
print()
print("Two numbers check")
a=int(input("Enter a number"))
b=int(input("Enter a number"))
if a>b:
    print(a,"greater than",b)
elif a<b:
    print(a,"less than",b)
else:
    print("Both are equal")
print()
print("Even or Add")
x=int(input("Enter a number"))
y=int(input("Enter a number"))
if x%2==0:
    print("The number is even")
else:
    print("The number is odd")
print()
print("positive,negative,zero")
a=int(input("Enter a number"))
b=int(input("Enter a number"))
if a>0:
    print("The number is positive")
elif a<0:
    print("The number is negative")
else:
    print("The number is zero")
print()
print("students mark and print")
mark=int(input("students mark"))
if mark>=90:
 print("Grade A")
elif 75>mark and  mark<=89:
 print("Grade B")
elif 50>mark and mark<=74:
 print("Grade C")
else:
 print("Fail")
print()
print("Leap year or not ")
y=int(input("Enter a year:"))
if (y%4==0):
 if (y100!=0) or (y%400==0):
  print(y,"is a leap year")
 else:
  print(y,"is not a leap year")
else:
  print(y,"is not a leap year")
print()
print("Eligible to vote")
age=int(input("Enter your age"))
if age>=18:
    print("You are eligible to vote")
else:    
    years_left=age-18
    print("You are not eligible to vote")
    print("Years are left to become eligible ")
print()
print("Largest three numbers")
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
num3=int(input("Enter a number"))
if (num1>=num2) and (num1>=num3):
    largest = num1
elif (num2>=num1) and (num2>=num3):
    largest = num2
else:
    largest = num3
print("The Largest among the number three is:", largest )
print()
print("Positive and Even")
a= int(input("Enter a number: "))
if a>0:
    if a%2==0:
        print("The Number is positive and even")
    else:
        print("It's an odd number")
else:
    print("It's a positive number or an even number")
print()
print("Nested if for child and age")
age=int(input("Enter your age"))
if age<13:
    print("Child")
else:
    if age<= 19:
        print("Teen")
    else:
        if age<=59:
            print("Adult")
        else:
            print("Senior Citizen")
print()
print("Vowels or consonants")
x= input("Enter a alphabet: ")
vowel = ['a','e','i','o','u','A','E','I','O','U']
if x in vowel:
    print("Vowel")
elif x.isalpha():
    print("Consonant")
else:
    print("Please enter a valid alphabet")
print()    
print("Pass/Fail")
a1 = int(input("Enter your Maths Mark: "))
a2 = int(input("Enter your Science Mark: "))
a3 = int(input("Enter your Social Mark: "))
total = a1+a2+a3
if a1>=40 and a2>=40 and a3>=40:
    print("Pass")
    avg = total/3
    if avg >= 90:
        print("Outstanding")
else:
    print("Fail")
    



