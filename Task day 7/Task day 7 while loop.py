print("print numbers from 10 down to 1")
i=10
while i>=1:
    print(i)
    i=i-1
print()
print("Sum of even digits in a number ")
num=int(input("Enter a number"))
sum=0
while num>0:
    digit=num%10
    if digit%2==0:
        sum+=digit
    num//=10
print("Sum of even digits:",sum)
print()
print("Digits are in a number")
num=int(input("Enter a number"))
count=0
while num>0:
    num//=10
    count+=1
print("Numbers of digits: ",count)
print()
print("Palindrome")
num=int(input("Enter a number"))
t=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
if t==rev:
    print("Its a palindrome")
else:
    print("Its not a palindrome")
print()
print("Reverse of a number ")
num=int(input("Enter a number"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
    print("Reversed number:",rev)
print()
print("Fibonacci series upto 100")
a=0
b=1
while a<=100:
    print(a)
    a=b
    b=a+b
print()
print("Power of a number manually")
base=int(input("Enter a base number"))
exponent=int(input("Enter a exponent number"))
result=1
count=0
while count<exponent:
    result=result*base
    count=count+1
    print("Result:",result)
print()
print("Dividing a number by 2 until it becomes less than 1 and count many divisions")
num=int(input("Enter a number"))
count=0
while num>=1:
    num=num//2
    count=count+1
    print("Number of divided:",count)
print()
print("Print the digits of a number from last to first,one per line")
num=int(input("Enter a number"))
while num>0:
    digit=num%10
    print(digit)
    num=num//10
print()
print("Sum of squares of digits of a number")
num=int(input("Enter a number"))
total=0
while num>0:
    digit=num%10
    total=total+(digit*digit)
    num=num//10
    print("Sum of squares of digits:",total)










    
    




      
