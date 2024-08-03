# if statement
# print a number is positive or negative
'''
n=int(input("Enter a number : "))
if(n>0):
    print("%s is positive" %n)
elif(n==0):
    print("%s is neither positive nor negative" %n)
else:
    print("%s is negative" %n)
'''
# check the eligibility to vote
'''
age=int(input("Enter age : "))
if(age>=18):
    print("%s is eligibile to vote" %age)
else:
    print("%s is not eligible to vote" %age)
'''
#check the number is even or odd
'''
n=int(input("enter a number : "))
if(n%2==0):
    print("%s is even number" %n)
else:
    print("%s is odd number" %n)
'''
# Find the big number among two numbers
'''
a=int(input("Enter A : "))
b=int(input("Enter B : "))
if(a>b):
    print("%s is big" %a)
    print("%s is bigger than %s" %(a,b))
else:
    print("%s is big" %b)
    print("%s is bigger than %s" %(b,a))
'''
# Big number among three numbers
'''
a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))
if (a>b and a>c):
    print("%s is bigger than %s and %s" %(a,b,c))
elif(b>c):
    print("%s is bigger than %s and %s" %(b,a,c))
else:
    print("%s is bigger than %s and %s" %(c,a,b))
'''
#Student marks
'''
marks=int(input("Enter marks : "))
if(marks>=90 and marks<=100):
    print("A grade")
elif(marks>=80 and marks<90):
    print("B grade")
elif(marks>=70 and marks<80):
    print("C grade")
elif(marks>=60 and marks<70):
    print("D grade")
elif(marks>=0 and marks<60):
    print("FAIL")
else:
    print("Invalid Input")
'''
#To print a number among 1 to 5 numbers as string
'''
a=int(input("Enter number : "))
if(a==1):
    print("ONE")
elif(a==2):
    print("TWO")
elif(a==3):
    print("THREE")
elif(a==4):
    print("FOUR")
elif(a==5):
    print("Five")
else:
    print("Invalid Input")
'''
#Obtaining the opted color according to the given color
'''
a=input("Enter the color : ")
if(a=="red"):
    print("Opted red color")
elif(a=="green"):
    print("Opted green color")
elif(a=="black"):
    print("Opted black color")
elif(a=="white"):
    print("Opted white color")
elif(a=="blue"):
    print("Opted blue color")
else:
    print("Invalid Input")
   '''
#Numbers 0-9,Small alphabets a-z, Capital alphabets A-Z and special Characters
'''
A=int(input("Enter a number : "))
if(A>=0 and A<=9):
    print("Typed Integer")
else:
    print("Invalid Input")
B=input("Enter a character : ")
if(B>="a" and B<="z"):
    print("Typed small Alphabet")
elif(B>="A" and B<="Z"):
    print("Typed capital Alphabet")
else:
    print("Invalid Input")
c=input("Enter a Special Character : ")
if c in ["!","@","#","$","%","^","&","*","`","~",")","(","-","_","=","+",",","<",">",".","/","]","[","}","{",";",":",'"',"'","\",","|","?"]:
    print("Typed Special Character")
else:
    print("Invalid Input")
'''
#
'''
A=input("Enter your input : ")
if(A>="a" and A<="z"):
    print("Typed small alphabets")
elif(A>="A" and A<="Z"):
    print("Typed capital alphabet")
elif A in ["!","@","#","$","%","^","&","*","`","~",")","(","-","_","=","+",",","<",">",".","/","]","[","}","{",";",":",'"',"'","\",","|","?"]:
    print("Typed special chracter")
else:
    print("Invalid Input")
'''
#uname=jaswanth pw=1234
'''
uname=input("Enter the username : ")


if(uname=="jaswanth"):
    print("Correct password")
    pw=int(input("Enter password : "))
    if(pw==1234):
        print("Correct password")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")
'''
#uname=jaswanth pw=1234
'''
uname=input("Enter the username : ")
pw=int(input("Enter password : "))
if(uname=="jaswanth" and pw==1234):
    print("Correct username and password")
else:
    print("Incorrect username and/or password")
'''
#for loop without using range() function
'''
list1=[24,37,85,49,59,71,20]
for i in list1:
    print(i)
print("Next statement after for loop")
'''
#Sum of elements in the list without using pre-defined function
#Method 1
'''
list1=[24,37,85,92,43,61,77]
print("sum :", sum(list1))
'''
#Method 2
'''
list1=[24,37,85,92,43,61,77]
s=0
for i in list1:
    s=s+i
print("sum :",s)
'''
#Search an element in a list
#Method 1
'''
list1=[24,37,85,92,43,61,77]
search=int(input("Enter a number to search :"))
if(search in list1):
    print("%s is found" %search)
else:
    print("%s is  not found" %search)
'''
#Sum of even and odd elements in a list
'''
list1=[24,37,85,92,43,62,77]
se=0
so=0
for i in list1:
    if(i%2==0):
        se=se+i
    else:
        so=so+i
print("Sum of even numbers :" ,se)
print("Sum of odd numbers :" ,so)
'''
#Print first n-numbers
'''
n=int(input("Enter a number : "))
for i in range(1,n+1):
      print(i)
'''
#Sum of n-numbers
'''
n=int(input("Enter a number : "))
s=0
for i in range(1,n+1):
    s=s+i
print("Sum :",s)
'''
#Print math table
'''
n=int(input("Enter a number : "))
for i in range(1,11):
    print("%s X %s = %s" %(i,n,i*n))
'''
#Prime number
'''
n=int(input("Enter a number : "))
fc=0
for i in range(1,n+1):
    if(n%i==0):
        fc=fc+1
if(fc==2):
    print("%s is a prime number" %n)
else:
    print("%s is not a prime number" %n)
'''
#Find the factorial of a number
'''
n=int(input("Enter a number : "))
s=1
for i in range(1,n+1):
    s=s*i
print("The factorial of %s is %s" %(n,s))
'''
#Math table in descending order
'''
n=int(input("Enter a number : "))
for i in range(10,0,-1):
    print("%s X %s = %s" %(i,n,i*n))
'''
#Sum of even numbers and odd numbers between n1 and n2
#Method 1
'''
n1=int(input("Enter the first number : "))
n2=int(input("Enter the last number : "))
se=0
so=0
for i in range(n1,n2+1):
    if(i%2==0): #Using an if-statement to find whether the given number is even 
        se=se+i
    else:
        so=so+i
print("The sum of even numbers between %s and %s is %s" %(n1,n2,se))
print("The sum of odd numbers between %s and %s is %s" %(n1,n2,so))
'''
#Method 2
'''
n=[]
print("Enter 5 elements for the list: ")
for i in range(5):
    val=int(input())
    n.append(val)
se=0
so=0
for i in range(5):
    if n[i]%2==0:
        se=se+n[i]
    else:
        so=so+n[i]
print("\nSum of Even Numbers is", se)
print("\nSum of odd Numbers is", so)
'''
#for in for
#1.for printing i
'''
for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()
'''
#2.for printing j
'''
for i in range(1,5):
    for j in range(1,5):
        print(j,end=" ")
    print()
'''
#3.for printing *
'''
for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()
'''
#4.for printing co-ordinates
'''
for i in range(1,5):
    for j in range(1,5):
        print((i,j))
    print()
'''
#
'''
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
'''
#
'''
for i in range(0,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
#
'''
for i in range(1,5):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
'''
#
'''
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
#
'''
for i in range(1,5):
    for j in range(5-i,0,-1):
        print(j,end=" ")
    print()
'''
#print prime numbers between the range of numbers
'''
n1=int(input("Enter N1 :"))
n2=int(input("Enter N2 :"))
for n in range(n1,n2+1):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        print(n)
'''
#for loop with else statement
'''
for i in range(1,10):
    print(i)
else:
    print("This is the else part")
print("Next statement after for loop")
'''
#while loop
#To print first n-numbers using while loop
'''
n=int(input("Enter a Number :"))
i=0
while(i<=n):
    print(i)
    i=i+1
'''
#Sum of first n-numbers in while loop
'''
n=int(input("Enter a Number :"))
i=1
s=0
while(i<=n):
    s=s+i
    i=i+1
print("Sum :",s)
'''
#Palindrome string
'''
name=input("Enter a Name:")
if(name==name[::-1]):
   print("%s is a palindrome string" %name)
else:
    print("%s is not a palindrome string" %name)
'''
#Factorial of a number using while loop
'''
n=int(input("Enter a number :"))
i=1
s=1
while(i<=n):
   s=s*i
   i=i+1
print("The factorial of %s is %s" %(n,s))
'''
#Prime number using a while loop
'''
n=int(input("Enter a number :"))
i=1
s=0
while(i<=n):
   if(n%i==0):
      s=s+1
   i=i+1
if(s==2):
   print("%s is a prime number" %n)
else:
   print("%s is not a prime number" %n)
'''
#Math table using while loop
'''
n=int(input("Enter a number :"))
i=1
while(i<=10):
   print("%s x %s = %s" %(i,n,i*n))
   i=i+1
'''
#Reverse math table using
'''
n=int(input("Enter a number :"))
i=10
while(i>0):
   print("%s x %s = %s" %(n,i,n*i))
   i=i-1
'''
#Sum of even and odd numbers using while loop
'''
n1=int(input("Enter the first number :"))
n2=int(input("Enter the last number :"))
i=n1
se=0
so=0
while(i<=n2):
   if(i%2==0):
      se=se+i
   else:
      so=so+i
   i=i+1
print("The sum of even numbers is %s" %se)
print("The sum of odd numbers is %s" %so)
'''
#Strong number
'''
n=int(input("Enter a number :"))
temp=n
s=0
while(n>0):
    d=n%10
    f=1
    for i in range(1,d+1):
        f=f*i
    s=s+f
    n=n//10
if(temp==s):
    print("%s is a strong number" %temp)
else:
    print("%s is not a strong number" %temp)
'''
#break statement -- when break executes it terminates the loop permanntly
'''
for i in range(1,10):
    if(i==5):
        break
    print(i)
'''
#continue statement -- when continue executes, it skips the statements after continue in that iteration, next iteration will continue as usual
'''
for i in range(1,10):
    if(i==5):
        continue
    print(i)
'''
#continue statement -- To skip 2 two numbers in the given range
'''
for i in range(1,10):
    if(i==5 or i==8):
        continue
    print(i)
'''
#pass statement -- do nothing
'''
for i in range(1,10):
    if(i==5):
        pass
    print(i)
'''
#break statement -- for-else condition
'''
for i in range(1,10):
    if(i==15):
        break
    print(i)
else:
    print("This is else part")
'''
#HW
#
#Python Dictionary
#To access keys in dictionary
'''
A={"Name":"Yash","Age":22,"Year":2001}
for i in A.keys():
    print(i)
''' 
#To access values in dictionary
'''
A={"Name":"Yash","Age":22,"Year":2001}
for i in A.values():
    print(i)
'''
#To access both keys and values
'''
A={"Name":"Yash","Age":22,"Year":2001}
for k,v in A.items():
    print(k,":",v)
'''
#
'''
A={"Name":"Yash","Age":22,"Year":2001}
search=input("Enter a key to search :")
found=False
for i in A.keys():
    if(i==search):
        found=True
        break
if(found==True):
    print("%s key is found and the value is %s" %(search,A[search]))
else:
    print("%s key is not found" %search)
'''
#Creating a list
'''
l1=[]
n=int(input("How namy elements you require to enter into a list :"))
for i in range(1,n+1):
    num=int(input("Enter a number :"))
    l1.append(num)
print(l1)
'''
#Creating a dictionary
'''
d1={}
n=int(input("How namy key,value pairs you require :"))
for i in range(1,n+1):
    k=int(input("Enter key :"))
    v=input("Enter value :")
    d1[k]=v
print(d1)
'''
#
dict1={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
#fruits = ["apple", "banana", "orange"]
#delimiter = ", "
result = delimiter.join(dict1)

print(result)
