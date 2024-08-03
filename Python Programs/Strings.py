#HW on string 7/4/23
#Replace all occurrences of ‘a’ with ‘$’ in a string
#Method-1
'''
str1=input("Enter a String :")
str2=str1.replace("a","$") # replace(old str,new str)
print(str2)
'''
#Method-2
'''
str1=input("Enter a string :")
str2=" "
for i in range(0,len(str1)):
    if(str1[i]=="a"):
        str2=str2+"$"
    else:
        str2=str2+str1[i]
print(str2)
'''
#Count the number of vowels in a string
#Method-1
'''
A=input("Enter a string :")
Vowels=["a","e","i","o","u"]
count=0
for i in range(len(A)):
    if A[i] in Vowels:
        count=count+1
print("Number of vowels in A are %s" %count)
'''
#Method-2
'''
A=input("Enter a string :")
count=0
for i in range(len(A)):
    if(A[i]=="a" or A[i]=="e" or A[i]=="i" or A[i]=="o" or A[i]=="u"):
        count=count+1
print("Number of vowels in A are %s" %count) 
'''
#Take a string and replace every blank space with a hyphen
#Method-1
'''
A=input("Enter a string :")
B=A.replace(" ","-")
print(B)
'''
#Method-2
'''
A=input("Enter a string :")
B=""
for i in range(0,len(A)):
    if A[i]==" ":
        B=B+"-"
    else:
        B=B+A[i]
print(B)
'''
#Calculate the length of a string without using library functions
'''
A=input("Enter a string :")
B=0
for i in A:
    B=B+1
print(B)
'''
#Calculate the number of words and characters present in a string
'''
A=input("Enter a string :")
B=0 #Characters
C=1 #Words
for i in A:
    B=B+1
    if(i==" "):
        C=C+1
print("Number of characters in A are %s" %B)
print("Number of world in A are %s" %C)
'''
#Count the number of lowercase letters and uppercase letters in a string
'''
A=input("Enter a string :")
B=0
C=0
for i in range(len(A)):
    if(A[i].isupper()):
        B=B+1
    elif(A[i].islower()):
        C=C+1
print("Number of uppercase letters are %s" %B)
print("Number of lowercase letters are %s" %C)
'''
#Check if a string is a palindrome or not
'''
A=input("Enter a string :")
if A==A[::-1]:
    print("%s is  a palindrome string" %A)
else:
    print("%s is not a palindrome string" %A)
'''
#Calculate the number of digits and letters in a string
'''
A=input("Enter a string :")
B=0
C=0
for i in A:
    if (i>="0" and i<="9"):
        B=B+1
    elif(i>="a" and i<="z"):
        C=C+1
print(B)#digits
print(C)#letters
'''
#Count the occurrences of each word in a given string sentence

#Check if a substring is present in a given string.
'''
A=input("Enter the string sentence :")
B=input("Enter the substring :")
if B in A:
    print("Yes the substring is present in the given string")
else:
    print("No the substring is not present in the given string")
'''
