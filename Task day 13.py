print("\nLoop tasks:")
print("\nWrite a python program to find and print all prime numbers between 1 and 100 using a for loop.at the end,print the total count of prime numbers:")
count=0
for i in range(1,101):
    if i==2 or i==3 or i==5 or i==7:
         print(i)
         count+=1
    elif i!=1 and i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
        print(i)
        count+=1
print("Total count of prime number:",count)

print("\nWrite a program to print the following pyramid pattern using nested for loops:")
for i in range(1,6):
    for j in range(6-i):
        print(end=" ")
    for k in range(1,i+1):
         print(k,end="")
    for k in range(i-1,0,-1):
         print(k,end="")
    print()

print("\nWrite a python program to calculate the electricity bill based on the following conditios:")
("units consumed rate per 0-100           $1.5 101-200         $2.5 201-300         $4.0 Above 300       $5.0 if total bill is above $1000-add 10% surcharge") 
units=int(input("Enter units consumed:"))
total=0
if units<100:
    total=1.5
elif units<=200:
    total=2.5
elif units<=300:
    rate=4.0
elif units>300:
    total=5.0
else:
    print("Enter valid data")
if total>1000:
    sur=total*0.10
    total=total+sur
print("Total charge:",total)

print("\nWrite a python program to print this diamond pattern using nested for loops:")
n=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))

print("\nWrite a python program using nested for loops to print the multiplication table(1-10)in grid format:")
for i in range(1,11):
    for j in range(1,11):
        print(f"{i*j:4}",end="")
    print()
print("\nWrite a python program to print pascal's triangle up to n rows:")
n=int(input("Enter a number of rows:"))
for i in range(n):
    print(" "*(n-i),end="")
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
    print()    
    

