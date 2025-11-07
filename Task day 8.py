print("Concantenate a given string to the end of another string")
a=input("Enter a string:")
b=input("Enter a string:")
s=a+b
print(s)
print()
print("Given string contains the specified sequence of char values:")
x=input("Enter a string:")
y=input("Enter a specified character to check:")
if y in x:
    print(x,"contains",y)
else:
    print(x,"not contains",y)
print()
print("To convert all characters in a string to lowercase:")
s=input("Enter a string:")
t=(s.lower(),"convert lower case")
print(t)
print()
print("To trim any leading or trailing whitespace from given a string: ")
a=input("Enter a string:")
b=a.strip()
print(b)
print()
print("To reverse a string:")
name=input("Enter a string:")
print(name[::-1])
print()
print("Replace all spaces with underscores:")
n="Electronics and communication"
t=n.replace("and","&")
print(t)
print()
print("A string made of the middle three characters")
c="python123"
l=len(c)
mid=l//2
print(c[mid-1:mid+2])
print()
print("Convert the first and last letter to capital:")
a=input("Enter a string:")
b="".join([i for i  in a if not i.isdigit()])
print(a[0].upper()+a[1:-1]+a[-1].upper())
print()
print("Program to get the length of a given string:")
name=input("Enter a number:")
len=len(name)
print("length of a name:",len)
print()
print("No of occurrence of a given string with repetition:")
a="I am new to this office but not new to remove digits in strings"
b="new"
print(a.count(b))
print()
print("To count number of words in a string:")
a=input("Enter a string:")
b=a.split()
print("length of the string:",count)
print()
print("To replace a specified character with another character:")
a="The quick brown fox jumps over the lazy dog"
b="dog"
c="fog"
r=a.replace(b,c)
print(r)
print()
print("Count vowels in a string:")
s=Engineering
vowels="aeiouAEIOU"
count=sum(1 for i in s if i in vowels)
print(count)
print()
print("Check if string contains only whitespace:")
a=""
print(s.isspace())
print()
print("Remove all digits from string:")
a="abcd1234"
print("".join([i for i in s if not i.isdigit]))
print()
print("Find the length of a name:")
name="abirami"
print(len(name))
print()
print("convert to upper case:")
name="abirami"
print(name.upper())
print()
print("Convert to lower case:")              
name="python"              
print(name.lower())
print()
print("Count letter a:")
name="apple"
print(name.count("a"))
print()
print("Check if starts with hello:")
name="helloworld"
print(name.startswith("hello"))
print()
print("Check if ends with .com:")
name="examle@gmail.com"
print(name.endswith(".com"))              
print()              
print("Find the position of the python:")
s="i am learning python programming:"
print(s.find("python"))
print()
print("Relace java with python:")
s="i love java"
print(s.relpace("java,python"))              
print()
print("Remove spaces from both side:")
s="helloworld"
print(s.strip())
print()
print("Caiptalize first letter:")
s="python is fun"
print(s.capitalize())
print()
print("Split sentence into words:")
s="python is fun"
print(s.split())
print()
print("Join a list of words:")
s=["python","is","fun"]
print("".join(s))
print()
print("only alphabets:")
s="python"
print(s.isalpha())
print()
print("only digits:")
s="12345"
print(s.isdigit())
print()
print("letters and numbers:")
s="python3"
print(s.isalnum())
print()
print("All lowercase:")
s="python"
print(s.lower())
print()
print("All uppercase:")
s="PYTHON"
print(s.isupper())
print()
print("Swapcase:")
s="PytHoN"
print(s.swapcase())
print()
print("Convert the each word first letter to uppercase:")
s="python programming language:"
print(s.title())
print()
print("only spaces:")
s=""
print(s.isspace())
print()
print("Palindrome check")
s="mam"
if s==s[::-1]:
      print("Palindrome")
else:
    print("Not palindrome")
print()
print("Remove all digits:")
s="abcd1234xyz"
print("".join([i for i in s if not i.isdigit()]))
print()
print("Replace spaces with underscore:" )
s="python is fun"
print(s.replace("","_"))
print()
print("Extract only numbers:")
s="abcd1234xyz5678"
print("".join([i for i in s if i.isdigit()]))
print()
print("Words starting with capital lettes:")
s="Junior Data Analytics"
for word in s.split():
    if word[0].isupper():
        print(word)
print()
print("Count how many times each letters occurs:")
s="banana"
for ch in sorted(set(s)):
    print(ch,":",s.count(ch))
print()
print("Remove all puncutation marks from a sentence:")
import string
s="Hello!!! How are you???"
clean=''.join(ch for ch in s if ch not in string.puncutation)
print()
print("check email endswith @gmail.com")
email="example@gmail.com"
print(email.endswith("@gmail.com"))
print()
print("Reverse string without slicing:")
s="python"
rev=""
for ch in s:
    rev=ch+rev
    print(rev)


    
        
              
              
      
                    
              
              
              
              
              

      

    


              
              




      

    

