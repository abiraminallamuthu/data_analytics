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

print("\n")
