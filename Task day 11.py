print("\ntuple tasks:" )

print("\nWrite a python program to create a tuple:")
t=(1,2,3,"Apple",1.5,"a")
print("tuple",(t))
print(type(t))

print("\nPython program to find the size of a tuple:")
t=(1,2,3,"a","Apple",1.5)
print("Size of tuple:",len(t))

print("\nPython-sort tuples:")
a=("Apple","Mango","Pineapple","banana","Dragonfruits","grapes")
b=list(a)
b.sort()
print(tuple(b))

print("\nWrite a python program to create tuple with different types:")
t=(1,2,3,"a","Apple",1.5)
print(t)

print("\nWrite a python program to unpack tuple in several varibles:")
l=(12,34,67)
(a,b,c)=l
print("A value is",a)

print("\nPython program to convert a tuple to a string:")
l=(12,34,67)
s=str(l)
print(type(s))

print("\nWrite a python program to get the 4th element 4th element from last of a tuple:")
t=(1,2,3,"a","b","c","apple","mango",True,2.5)
print(t[3])
print(t[-4])

print("\nWrite a python program to find the repeated items of a tuple:")
t=(1,2,3,2,3,4,1,4)
repeated=[]
for i in t:
    if t.count(i)>1 and i not in repeated:
        repeated.append(i)
print("Repeated elements:",repeated)

print("\nWrite a python program to check whether an element exists within a tuple:")
t=(3,6,2,5,8)
x=int(input("Enter element to check: "))
if x in t:
    print(x,"exists in the tuple")
else:
    print(x,"doesn't exist in the tuple")
print()

print("\nWrite a python program to convert a list to a tuple:")
l=[1,2,3,4]
print(tuple(l))

print("\nWrite a python program to remove an item from a tuple:")
l=(1,2,3,4,5)
s=list(l)
s.remove(5)
print(s)

print("\nWrite a python program to slice a tuple:")
l=(1,2,3,4,5,6)
print("First Two Elements: ",l[:2])
print("Last Two Elements: ",l[-2:])

print("\nWrite a python program to find the index of an item of a tulpe:")
l=(1,2,3,4,5,6)
print(l.index(2))

print("\nWrite a python program to find the length of a tuple:")
t=(1,2,3,4,5,6)
print(len(t))

print("\nWrite a python program to reverse a tuple:")
t=(1,2,3,4,5,6)
print(t[::-1])

print("\nWrite a python program  convert a given string list to a tuple:")
l=['apple','orange','mango','pineapple']
print(tuple(l))



