print("\nReverse s given list in python:")
l=[100,200,300,400,500]
print(l[::-1])

print("\nConcatenate two lists:")
list1=["Hello","Madam"]
list2=["Dear","Sir"]
list=list1+list2
print(list)

print("\nRemove empty strings from the list of strings:")
list1=["Pen","","Pencil","Eraser","","Scale"]
for i in list1:
    if i=="":
        list1.remove("")
print(list1)


print("\nCheck if a list contains an element")
list=[1,2,3,'a','b','c']
n = input("Enter an element to check: ")
if n in list:
    print(f"{n} is present in the list")
else:
    print(f"{n} is not present in the list")

print("\nRemove all elements from a list:")
a=[1,2,3,"a","b","c"]
a.remove("a")          
print(a)          

print("\nCount the occurrence of a specific object in a list:")
pets=['dog','cat','fish','fish','cat']
a="fish"
b="cat"
print("Occurrence of fish:",pets.count(a))
print("Occurrence of cat:",pets.count(b))

print("\nReturn the length of a list:")
x=["Apple","Banana","Orange","Grapes","Mango"]
print(len(x))

print("\nInsert a value at specific index in an exisiting list:")
l=[16,21,23]
l.insert(1,17)
print(l)

print("\nWrite a python program to clone or copy list:")
a=["Apple","Banana","Orange","Grapes","Mango"]
b=a.copy()
print(b)

print("\nWrite a python program to extend a list without append:")
a=[1,2,3]
b=[3,2,1]
a.extend(b)
print(a)

print("\nRemove duplicats from a list:")
a=[3,2,2,1,1,1]
print(set(a))

print("\nFind the index of the 1st matching element:")
a=[1,2,3,4,5]
print(a.index(1))

print("\nCheck if an elements not in a list:")
l=[1,2,3,"a","b","c"]
print(l)
print("z not in list:",'z' not in l)

print("\nPython program to create a list of 5 numbers and print it:")
l=[]
n=int(input("Enter number of elements"))
for i in range(n):
    e=input("Enter a value:")
    l.append(e)
print(l)

print("\nWrite a program to find the length of a list using len()")
l=[1,2,3,4,5]
print(len(l))

print("\nProgam to access elements from a list using positive or negative indexes:")
l=[1,2,3,"a","b","c"]
print(l[1:-1])

print("\nWrite a program to update the 3rd elements of a list:")
l=[1,2,3,"a","b","c"]
print(l)
l[2]=65
print(l)

print("\n Write a program to delete an element from a list")
l=['a','b','c','d','e']
print(l)
l.remove('b')
print(l)

print("\nWrite a program to append a new element to the list using append().")
l=['a','b','c','d','e']
print(l)
l.append('f')
print(l)

print("\nWrite a program to insert an element at a specific position using insert().")
l=['a','b','c','d','e']
print(l)
l.insert(0,'r')
print(l)

print("\nWrite a program to remove an element using remove().")
l=['a','b','c','d','e']
print(l)
l.remove('b')
print(l)

print("\nWrite a program to remove the last element using pop().")
l=['a','b','c','d','e']
print(l)
l.pop()
print(l)

print("\nWrite a program to clear all elements using clear().")
l=['a','b','c','d','e']
print(l)
l.clear()
print(l)

print("\nWrite a program to print all elements of a list using a for loop.")
l=['a','b','c','d','e']
for i in l:
    print(i)

print("\nWrite a program to find the sum of all elements using sum().")
l= [10, 20, 30, 40]
print(l)
total = sum(l)
print(total)

print("\nWrite a program to find the maximum and minimum values using max() and min().")
l=[1,2,3,4,5]
print(l)
b=max(l)
c=min(l)
print("Max:",c)
print("Min:",b)

print("\nWrite a program to count how many times an element appears using count().")
l=['a','a','b','b','b','c']
print(l)
print(l.count('a'))

print("\nWrite a program to find the index of a specific element using index().")
l=['a','b','c']
print(l)
print(l.index('b'))

print("\nWrite a program to reverse a list using reverse().")
l=[1,2,3,4,5]
l.reverse()
print(l)

print("\nWrite a program to sort a list in ascending and descending order using sort().")
l=["abirami","nethra","apple","Banana"]
l.sort()
print(l)
l=["abirami","nethra","apple","Banana"]
l.sort(reverse=True)
print(l)

print("\nWrite a program to copy one list to another using copy().")
a=[1,2,3]
print(a)
b=a.copy()
print(b)

print("\nWrite a program to print only even numbers from a list.")
l=[1,2,3,4,5,6]
print(l)
for i in l:
    if i%2==0:
        print(i)

print("\nWrite a program to print only odd numbers from a list.")
l=[1,2,3,4,5,6]
print(l)
for i in l:
    if i%2!=0:
        print(i)

print("\nWrite a program to add two lists using + operator.")
l1=[1,2,3]
l2=[4,5,6]
print(l1)
print(l2)
print(l1+l2)

print("\nWrite a program to repeat list elements using * operator.")
a=[1,2,3]
print(a)
b=a*2
print(b)

print("\nWrite a program to check if an element exists in a list using in.")
l=[1,2,3,"a","b","c"]
print(l)
print("a in list:",'a' in l)

print("\nWrite a program to slice a list (print first 3 and last 3 elements).")
l=[1,2,3,4,5,6]
print(l)
print(l[:3])
print(l[-3:])

print("\nWrite a program to find the largest 2 numbers in a list.")
l=[16,43,92,76,30]
l.sort(reverse=True)
print(l)
print("largest numbers:",l[0:2])

print("\nWrite a program to find duplicate elements in a list.")
l=[1,1,2,4,4,5,7]
dup=[]
for i in l:
    if l.count(i)>1 and i not in dup:
        dup.append(i)
print(dup)

print("\nWrite a program to remove duplicate elements from a list.")
l=[1,1,2,3,4,4]
print(l)
print(list(set(l)))

print("\nWrite a program to merge two sorted lists into one sorted list.")
l1=[1,4,32,67,34]
print(l1)
l2=["a","B","g","F","y"]
print(l2)
l1.sort()
l2.sort(key=str.lower)
l3=l1+l2
print(l3)

print("\nWrite a program to create a list of squares of numbers from 1 to 10 using a loop.")
sq=[]
for i in range(1,11):
    i*=i
    sq.append(i)
print(sq)
    
print("\nWrite a program to separate even and odd numbers into two lists.")
l1=[]
l2=[]
for i in range(1,11):
    if i%2==0:
        l1.insert(i,i)
    else:
        l2.insert(i,i)
print(l1)
print(l2)

print("\nWrite a program to find common elements between two lists.")
l1=[1,2,3,4,5]
l2=[2,4,6,9,0]
print(l1)
print(l2)
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)

print("\nWrite a program to find elements present in one list but not in another.")
l1=[1,2,3,4,5]
l2=[2,4,6,9,0]
print(l1)
print(l2)
l3=[]
for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)

print("\nWrite a program to remove all occurrences of a specific element from a list.")
l=[1,1,2,2,2,3,4,4]
print(l)
l1=[]
for i in l:
    if i!=2:
        l1.append(i)
print(l1)

print("\nWrite a program to convert a list into a tuple.")
l=[1,2,3]
print(tuple(l))

print("\nWrite a program to find the average of list elements.")
l=[]
add=0
n=int(input("Enter number of elements"))
for i in range(n):
    e=int(input("Enter a value:"))
    l.append(e)
    add+=e
print(l)
print("Sum:",add)
print("average:",add/n)

print("\nWrite a program to count positive, negative, and zero numbers in a list.")
l=[-2,-1,0,1,2,3,4]
print(l)
zerocount=0
poscount=0
negcount=0
for i in l:
    if i==0:
        zerocount+=1
    elif i>0:
        poscount+=1
    else:
        negcount+=1
print(zerocount)
print(poscount)
print(negcount)

print("\nWrite a program to find product of all elements in a list (without using math.prod()).")
l=[1,2,3,4,5]
pro=1
for i in l:
    pro*=i
print(pro)

    
    








