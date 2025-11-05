print("Print all numbers between 1 and 100 that are divisible by 6 but not by  9")
for i in range(1,101):
    if i%6==0 and i%9!=0:
        print(i)
print()
print("Sum of all odd numbers from 1 to 50")
total=0
for i in range(1,51):
    if i%2!=0:
        total=total+i
        print("Sum of all odd nmbers from 1 to 50:",total)
print()
print("Count how many numbers b/w 1 and 200 are divisible by both 4 and 6")
count=0
for i in range(1,201):
    if i%4==0 and i%6==0:
        count=count+1
        print("Count of numbers divisible by both 4 and 6:",count)
print()
print("Print the multilication table of a given number by n(from 1 to 10)")
n=int(input("Enter a number"))
print( "multilpication of table of",n)

for i in  range(1,11):
    print(n,"x",i,"=",n*i)
print()
print("Factorial of a given number n")
n=int(input("Enter a number"))
fact=1
for i in range(1,n+1):
    fact=fact+i
    print("Factorial of",n,"is:",fact)
print()
print("Print all prime numbers between 1 and 50")
for num in range(1,51):
    if num==2 or num==3 or num==5 or num==7:
        print(num)
    elif num>1 and num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0:
        print(num)
print()
print("Sum of the digits of a number using arithmetic only")
a=int(input("Enter a value"))
tot=0
for i in range(1,a):
   tot=i+tot
   print(tot)
print()
print("Calculate how many numbers between 1 and 500 are perfect cubes")
for i in range(1,501):
    cube=i**3
    if cube<=500:
        print(i,"=",cube)
print()
print("Print the reverse of a number")
num=input("enter a number")
rev=""
for i in num:
    rev=i+rev
    print(rev)
print()
print("Print numbers from 1 to 100 but skip numbers ending with digit 5")
for i in range(1,101):
    if i%10!=5:
        print(i)
    

   

            
    


