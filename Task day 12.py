print("\nList Tasks:")

print("\nCreate a list of 5 of your favourite fruits:")
l=["Apple","Banana","Orange","Mango","Grapes"]
print(l)

print("\nAdd a new fruit to the list using a list method: ")
l=["Apple","Banana","Orange","Mango","Grapes"]

l.append("Guva")
print(l)

print("\nRemove one fruit from the list:")
l=["Apple","Banana","Orange","Mango","Grapes"]
l.remove("Grapes")
print(l)

print("\nPrint the number of fruits in your list:")
l=["Apple","Banana","Orange","Mango","Grapes"]
a=len(l)
print(a)

print("\nPrint all the fruits one by one using a for loop:")
l=["Apple","Banana","Orange","Mango","Grapes"]
for i in l:
    print(i)

print("\nReverse the list and print it:")
l=["Apple","Banana","Orange","Mango","Grapes"]
l.reverse()
print(l)

print("\nSort the list alphabetically and print it:")
l=["Apple","Banana","Orange","Mango","Grapes"]
l.sort()
print(l)

print("\nCheck if a particular (like Apple) is in the list:")
l=["Apple","Banana","Orange","Mango","Grapes"]
if "Apple" in l:
    print("In this list in apple is present")
else:
    print("In this list in apple is not present")

    
