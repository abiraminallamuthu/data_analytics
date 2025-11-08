print("Pattern task:")
print("Program to print left triangle:")
for i in range(5):
    for j in range(1,5-i):
      print(" ",end=" ")
    for k in range(0,i+1):
      print("*",end=" ")
    print()

print()
print("Program to print right triangle:")
for i in range(1,4):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


print()
print("Program to print square:")
for i in range(1,4):
    for j in range(1,4):
      print("*",end=" ")
    print()

print()
print("Program to Print hollow square:")
for i in range(4):
    for j in range(4):
        if (i in{1,2} and j in{1,2}):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

print()
print("To print inverse left triangle:")
for i in range(4,0,-1):
    for k in range(4-i):
       print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

print()
print("To print inverse right triangle:")
for i in range(1,6):
    for j in range(6-i):
        print("*",end=" ")
    print()
    
print()
print("To Print Increasing Number Triangle:")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("To Print Decreasing Number Triangle:")
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("To Print Right Aligned Decreasing Numbers:")
for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
print("To Print Alphabet Triangle:")
ch = 65
for i in range(5):
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("To Print Repeated Alphabet Triangle:")
ch = 65
for i in range(1,6):
    for j in range(i):
        print(chr(ch),end=" ")
    print()
    ch+=1
print("To Print Continuous Alphabet Triangle:")
ch = 65
for i in range(5):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()
print("To Print Eight patterns:")
for i in range(7):
    for j in range(5):
        if (i in {0,3,6} and j in {1,2,3}) or (j in {0,4} and i not in {0,3,6}):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()    
    



    
  


    

    

