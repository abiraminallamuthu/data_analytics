print("positive,negative,or zero")
a=int(input("Enter a number :"))
if(a>0):
 print("positive")   

elif(a<0):
  print("negative")

else:
 print("The number is zero")
 
num=int(input("Enter a number:"))
if num%2==0:
 print(num,"is even")        
else:
 print(num,"is odd")
age=int(input("Enter your age:"))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
marks=int(input("Enter your marks:"))
if  marks>=40:
          print("you have the exam pass")
else:
      print("you have the exam fail")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1>num2:
  print("The largest number is:",num1)
elif num2<num1:
      print("The lagest number is:",num2)
stu_mark=int(input("Enter a total mark:"))
if stu_mark>90 and stu_mark<=100:
    print("A Grade")
elif stu_mark>80 and stu_mark<=70:
    print("B Grade")
elif stu_mark>60 and stu_mark<=50:
     print("C Grade")
elif stu_mark>40 and stu_mark<=30:
    print("D Grade")
else:
    print("fail")
day_number=int(input("Enter a number 1-7:"))
if day_number==1:
    print("Sunday")
elif day_number==2:
    print("Monday")
elif day_number==3:
    print("Tuesday")
elif day_number==4:
    print("Wednesday")
elif day_number==5:
    print("Thursday")
elif day_number==6:
    print("Friday")
elif day_number==7:
    print("Saturday")
else:
    print("Invalid")
a=input("Enter any character")
if a.isalpha():
    print("is an aiphabet")
elif a.isdigit():
    print("is an digit")
else:
    print("is an special character")
num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))
num3=int(input("Enter a number3:"))
if num1>=num2 and num1>=num3:
 print("num1 is greater than num2")
elif num2>=num1 and num2>=num3:
  print("num2 is greater than num3")
else:  
  print("The largest num is:")
temperature=input("Enter the temperature")
if temperature=="hot":
  print("Hot")
elif temperature=="warm":
  print("warm")
elif temperature=="cool":
  print("cool")
else:
    print("cold")
print("Positive and even usig nested if")
p = int(input("Enter a number: "))
if p>0:
    if p%2==0:
        print("The Number is positive and even")
    else:
        print("It's an odd number")
else:
    print("It's  a positive number nor an even number")
print("Login system")    
username = input("Enter your name: ")
password = input("Enter your password: ")
x = "Nethra"
y = "12345"
if x == username:
    if y == password:
        print("Login was successful")
    else:
        print("Incorrect password")
age = int(input("Enter your age: "))
exp = input("Do you have experience (type yes/no): ")
if age>18:
    if exp == "yes":
        print("You are eligible for the job")
    else:
        print("You must have experience")
else:
    print("You must be above 18")
year=int(input("Enter a leap year:"))
if(year%400==0):
    print(year,"leap year")
elif (year%100==0):
 print(year,"not in leap year")
marks = int(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))
if marks>80:
    if attendance>=95:
        print("You Qualify for the scholarship!")
    else:
        print("You need at least 95% attendance")
else:
    print("You need at least 80 marks") 
   



  
    
     
    
             


























        
