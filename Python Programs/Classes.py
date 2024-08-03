#Classes
'''
class sample: #Class declaration/definition
    def myfun1(self): #Method
        print("Hi Yaswanth how are you")
    def myfun2(self):
        print("Hi Abhishek how are you")
#program execution starts from here
obj1=sample()
obj1.myfun1()
obj1.myfun2()
obj2=sample()
obj2.myfun1()
obj2.myfun2()
print(type(obj1))
print(type(obj2))
'''
#
'''
class sample: #Class declaration/definition
    def inputvalues(self,a,b): #Methods
        self.a=a
        self.b=b
        print(a,b)
    def add(self):
        print(self.a+self.b)
#Program execution starts from here
yaswanth=sample()
shimlan=sample()
print("Marks of yaswanth :")
yaswanth.inputvalues(87,76)
print("Marks of shimlan :")
shimlan.inputvalues(95,89)
print("Total marks of yaswanth :")
yaswanth.add()
print("Total marks of shimlan :")
shimlan.add()
'''
#
'''
class sample: #Class declaration/definition
    def inputvalues(self,a,b): #Methods
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mul(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)
#Program execution starts from here
yaswanth=sample()
yaswanth.inputvalues(87,76)
yaswanth.add()
yaswanth.sub()
yaswanth.mul()
yaswanth.div()
'''
#Classes -- Constructor
'''
class sample: #Class declaration/definition
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("Sum :",self.a+self.b)
#Program execution starts from here
yaswanth=sample(84,97)
abhishek=sample(98,92)
yaswanth.add()
abhishek.add()
'''
#Classes -- Constructor
'''
class employee:
    def __init__(self,eno,ename,sal):
        self.eno=eno
        self.ename=ename
        self.sal=sal
    def display(self):
        print("Eno :",self.eno)
        print("Ename :",self.ename)
        print("Sal :",self.sal)
    def increment(self,sal):
        self.sal=sal
#Program execution starts here
vennela=employee(105,"Vennela AB",76358.96)
priya=employee(106,"Hari Priya",86259.45)
vennela.display()
priya.display()
vennela.increment(76358.96+((76358.96)*12/100))
priya.increment(86259.45+((86259.45)*10/100))
print("*************After Increment***********")
vennela.display()
priya.display()
'''
#instance and class(static) variables
#instance variable - defining variables inside "__init__".
#class variable - defining variables inside the class and outside "__init__".
'''
class cars:
    wheels=4 #class variable
    def __init__(self,company,milage): #init method or constructor
        self.company=company
        self.milage=milage #instance variables
    def output(self):
        print("Company :",self.company)
        print("Milage :",self.milage)
        print("Wheels :",cars.wheels) #or we can use self.wheels
#Program execution starts from here
c1=cars("Maruthi",22) #object decleration
c2=cars("Hyundai",18)
c1.output()
c2.output()
print("**************************")
c1.milage=25 #changing the instance variable
cars.wheels=3 #changine the class variable
c1.output()
c2.output()
'''
#Class inside Class
'''
class outer: #Outer class
    def __init__(self,ov):
        self.ov=ov
        self.in1=self.inner(88) #inner class object should be specified inside init
    class inner: #Inner class
        def __init__(self,iv):
            self.iv=iv
#Program execution starts from here
obj1=outer(5)
print("Outer class value",obj1.ov) #Print outer class value
print("Inner class value",obj1.in1.iv) #Print the value of inner class
'''
#Single inheritance
'''
class parent:
    def function1(self):
        print("This is function1 of parent :")
class child(parent):
    def function2(self):
        print("This is function2 of parent :")
#Program execution starts from here
c1=child()
c1.function1()
c1.function2()
p1=parent()
p1.function1()
'''
#Multilevel inheritance
'''
class Gparent:
    def function1(self):
        print("This is function1 of grand parent class")
class parent(Gparent):
    def function2(self):
        print("This is function2 of parent class")
class child(parent):
    def function3(self):
        print("This is function3 of child class")
#Program execution starts from here
c1=child()
c1.function1()
c1.function2()
c1.function3()
'''
#Multiple
'''
class parent1:
    def function1(self):
        print("This is function1 in parent1")
class parent2:
    def function2(self):
        print("This is function2 in parent1")
class child(parent1,parent2):
    def function3(self):
        print("This is function3 in child")
#Program execution starts from here
c1=child()
c1.function1()
c1.function2()
c1.function3()
'''
#HW -- (1+X^n+1)
'''
n=int(input("Enter a number :"))
s=1
print("%s+" %s,end="")
for i in range(0,n+1):
    print("(X^%s)" %(i+1),end="+")
print(end=".............(X^n)")
'''
#HW -- (1+nX^n+1)
'''
n=int(input("Enter a number :"))
s=1
a=1
print("%s+" %s,end="")
for i in range(0,n+1):
    print("(%sX^%s)" %((a+i),(i+1)),end="+")
'''
#Hierarchial inheritance
'''
class parent:
    def function1(self):
        print("This is function1 in class parent")
class child1(parent):
    def function2(self):
        print("This is function2 in class child1")
class child2(parent):
    def function3(self):
        print("This is function3 in class child2")
#Program execution starts from here
c1=child1()
c1.function1()
c1.function2()
c2=child2()
c2.function1()
c2.function3()
'''
#
'''
class Addition:
    def add(self,a,b):
        print(a+b)
class Subtraction:
    def subtract(self,a,b):
        print(a-b)
class Multiplication:
    def multiply(self,a,b):
        print(a*b)
class Division:
    def divide(self,a,b):
        print(a/b)
class Mathfunctions(Addition,Subtraction,Multiplication,Division):
    def moddivide(self,a,b):
        print(a%b)
class addsub(Addition,Subtraction):
    pass
#Program execution starts from here
c1=Mathfunctions()
c1.add(2,3)
c1.subtract(7,4)
c1.multiply(3,3)
c1.divide(9,2)
c2=addsub()
c2.add(14,88)
c2.subtract(74,55)
'''
#
'''
class Cashier:
    def cashtransactions(self):
        print("He deals cash transactions for class cashier")
class CRO:
    def customers(self):
        print("He deals customer services for class CRO")
class Asstmanager(Cashier,CRO):
    def loans(self):
        print("He deals loan services for class assistant manager")
class Manager(Asstmanager):
    def lockers(self):
        print("He deals with lockers for class manager")
#Program execution starts from here
c1=Manager()
c1.cashtransactions()
c1.customers()
c1.loans()
c1.lockers()
'''
#Constructors in single inheritance
'''
class Parent:
    def __init__(self):
        print("This is parent init")
    def function1(self):
        print("Parent class-this is function1")
class child(Parent):
    def __init__(self):
        super().__init__() #to access parent class
        print("This is child init")
    def function2(self):
        print("Child class-this is function2")
#Program execution starts from here
c1=child()
c1.function1()
c1.function2()
'''
#(MRO) Mutliple Resolution Order
'''
class Parent1:
    def __init__(self):
        print("This is parent1 init")
    def function1(self):
        print("This is function1")
class Parent2:
    def __init__(self):
        print("This is parent2 init")
    def function2(self):
        print("This is function2")
class child(Parent1,Parent2):
    def __init__(self):
        super().__init__()
        #super().__init__()
        print("This is child init")
    def function3(self):
        print("This is function3")
#Program execution starts from here
c1=child()
c1.function1()
c1.function2()
c1.function3()
'''
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
#How + operator will work on numbers
'''
a=15
b=7
print(a+b)
print(int.__add__(a,b))
print(a.__add__(b))
print(a-b)
print(int.__sub__(a,b))
print(a.__sub__(b))
'''
#How + operator will work on numbers
'''
a="anand"
b="kumar"
print(a+b)
print(a.__add__(b))
print(str.__add__(a,b))
'''
#Operator overloading
'''
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other): #Here self means s1 and other means s2
        m1=self.m1+other.m1 #m1=s1.m1+s2.m2
        m2=self.m2+other.m2 #m2=s1.m2+s2.m2
        s3=student(m1,m2)
        return s3
    def output(self):
        print(self.m1)
        print(self.m2)
#Program execution starts from here
s1=student(87,56)
s2=student(65,74)
s3=s1+s2 #s3=s1.__add__(s2)
s3.output()
'''
#Method overloading
'''
class sample:
    def add(self,a,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            s=a+b+c
        elif(a!=None and b!=None):
            s=a+b
        else:
            s=a
        return s
#Program execution starts from here
s1=sample()
print(s1.add(2,3,4))
print(s1.add(2,3))
print(s1.add(2))
'''
#Method overriding -- The parent class method will be override by child class method
'''
class parent:
    def output(self):
        print("This is parent output")
class child(parent):
    pass
obj1=child()
obj1.output()
'''
#This parent method was override by a child method
'''
class parent:
    def output(self):
        print("This is parent output")
class child(parent):
    def output(self):
        print("This is child output")
obj1=child()
obj1.output()
'''
#Polymorphism -- Duck typing
#if there is an object called "energy" and it has method "fuel" that is enough
#we are not concerned about which class object it is.
#we are concerned about it should have the method fuel
'''
class car:
    def fuel(self):
        print("Car runs with petrol")
        print("Car runs with diesel")
class bike:
    def fuel(self):
        print("Bike runs with petrol")
class ebike:
    def fuel(Self):
        print("Ebike runs with electricity")
for obj in car(),bike(),ebike():
    print("Data type of an object :", type(obj))
    obj.fuel()
'''
#Exception Error
#ZeroDivisionError: division by zero
'''
x=12
y=0
print(x/y)
print("End of the program")
'''
#
'''
x=12
y=0
try:
    print(x/y) #Called critical section
except Exception:
    print("You can't divide by zero")
print("End of the program")
'''
#With exception statement
'''
x=12
y=0
try:
    print(x/y) #called critical section
except Exception as ex:
    print("You can't divide by zero :",ex)
print("End of the program")
'''
#With finally statement
'''
x=12
y=0
try:
    print("Logic open")
    print(x/y) #Critical section
except Exception as ex:
    print("You can't divide by  zero:",ex)
else:
    print("This is else part")
finally:
    print("Logic close")
print("End of the program")
'''
#Reading a file
'''
fr=open("Samplefile.txt","r") #Mode -- read
print(fr.read())
#print(fr.readline())
#print(fr.read(16))
#data=fr.read()
#print(data)
'''
#Writing a file
#If the file exists, then the content in the file will be erasied and new data will be written
#If the file doesn't exists, then creates new file
'''
fw=open("Samplefile.txt","w") #Mode -- write
fw.write("Now we are discussing python \n")
fw.write("After this we are going to discuss pandas\n")
fw.write("Pandas is for data processing")
fw.close()
'''
#Creates the specified file, returns the error if it exists
'''
f=open("Samplefile1.txt","x")
f.write("\ncovid 19 suffering the world badly\n")
f.write("As of now Hyderabad is safe")
f.close()
'''
#Appending a file
'''
f=open("Samplefile1.txt","a") #Mode --- Append
f.write("\ncovid 19 suffering the world badly \n")
f.write("As of now Hyderabad is safe")
f.close()
'''
#File concepts using functions
'''
def fileread():
    f=open("Samplefile.txt","r")
    print(f.read())
def fileappend():
    f=open("Samplefile.txt","a")
    f.write("\n this is multi file concepts\n")
    f.write("we can do like this")
    f.close()
print("Program execution starts here")
fileread()
fileappend()
print("***************After appending the data***************")
fileread()
'''
#Iterators
list1=[15,30,45,60,75]
#usual way of fetching the values
#print(list1[2])#based on the index we are fetching the value from the list
#to fetch all values
'''
for i in list1:
    print(i)
'''
#
'''
it1=iter(list1)
print(it1.__next__())
print(it1.__next__())
print(it1.__next__(),it1.__next__(),it1.__next__())
'''
#
'''
for i in it1:
    print(1.__next__())
'''
#Generator
'''
def sample():
    return(14,25.58,"Yaswanth")
    return(11,58,69)#it can't be done -- because only one object is defined in the main program
    return(12)#it can't be done -- because only one object is defined in the main program
val=sample()
print(val)
#print(val.__next__())#it can't be done -- 'tuple' object has no attribute '__next__'
#print(val.__next__())#it can't be done -- 'tuple' object has no attribute '__next__'
'''
#
'''
def sample():
    yield(25,36,45)
    yield(116,"Yash",3.142)
    yield 33
values=sample()
#print(values)
print(values.__next__())
print(values.__next__())
print(values.__next__())
'''
#Top ten perfect squares
'''
def topten():
    n=1
    while n<=10:
        yield n*n
        n+=1
values = topten()
for i in values:
    print(i)
'''
#Decorators
#Method 1
'''
def div(a,b):
    print(a/b)
a=int(input("Enter A :"))
b=int(input("Enter B :"))
if (a>b):
      div(a,b)
else:
    a,b=b,a #Swaping
    div(a,b)
'''
#Method 2 -- using decorators
'''
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a #swaping
        return func(a,b)
    return inner
@smart_div #decortor
def div(a,b): #Actual function
    print(a/b)
div(6,2)
div(2,4)
'''
