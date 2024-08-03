#Function
'''
def sample(): #Function definition
    print("Hi Yaswanth how are you")
    print("Hi Abhishek how are you")
#Program execution starts from here
print("First statement to execute")
sample() #Function call
print("Next statement after function call")
'''
#Addition of two numbers using function
'''
def add(a,b): #function definition,a and b are called as arguments or parameters
    print("Sum :",a+b)
    print("Sub :",a-b)
    print("Mul :",a*b)
    print("Div :",a/b)
#Program execution starts from here
print("First statement to execute")
x=int(input("Enter X :"))
y=int(input("Enter Y :"))
add(x,y) #function call
print("Next statement after function call")
'''
#Area of a circle using a function
'''
def area_of_circle(r): #function definition,r is called as argument or parameter
    print("Area of circle :", (22/7)*r*r)
#Program execution starts from here
print("First statement to execute")
x=float(input("Enter radius :"))
area_of_circle(x) #function call
print("Next statement after function call")
'''
#Function with return
'''
def add(a,b):
    return(a+b)
#Program execution starts from here
print("First statement to execute")
x=int(input("Enter x :"))
y=int(input("Enter Y :"))
s=add(x,y)
print("Sum :",s)
print("Next statement after function call")
'''
#Function with return for calculating percentage interest
'''
def interest(p,t,r):
    i=(p*t*r)/100
    return(i)
#Program execution starts from here
p=int(input("Enter Amount :"))
t=int(input("Enter Time :"))
r=int(input("Enter Rate :"))
ist=interest(p,t,r)
print("Total amount to be paid :", p+ist)
'''
#Factorial using with args and with return
'''
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)
#Program execution starts from here
n=int(input("Enter a number :"))
fa=fact(n)
print("Factorial :", fa)
'''
#Factorial using with args and without return
'''
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print("Factorial :",f)
#Program execution starts from here
n=int(input("Enter a number :"))
fact(n)
print("Next statement after function call")
'''
#Factorial using without args and without return
'''
def fact():
    n=int(input("Enter a number :"))
    f=1
    for i in range(1,n+1):
        f=f*i
    print("Factorial :",f)
#Program execution starts from here
print("First statement")
fact()
print("Next statement after function")
'''
#Factorial using without args and with return
'''
def fact():
    n=int(input("Enter a number :"))
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)
#Program execution starts from here
print("First statement")
fa=fact()
print("Factorial :",fa)
'''
#nested functions
'''
def display(): #function definition
    print("This is display function")
    def show(): #function definition
        print("This is show function")
    show()#function call
#program execution starts here
print("First statement to execute")
display()#function call
print("Next statement after function call")
'''
#Passing different arguement types to the function
'''
def display(a,b): #function definition
    print(a+b)
#program execution starts here
print("First statement to execute")
display(15,68)#function call
display(15.69,78.15)
display("Yas","wanth")
display([105,874,965,488],[48,52,63,45])
print("Next statement after function call")
'''
#Passing function as an argument
'''
def display(sh):
    print("This is display function"+ " " +sh())

def show():
    return("This is show function")
#program execution starts here
display(show)
'''
#passing funtion as an argument and return the function
'''
def display(sh):
    print("This is display function")
    return(sh)

def show():
    return("This is show function")
#program execution starts here
r_sh=display(show)
print(r_sh())
'''
#Local variable
'''
def sample1():
    a=25 #Local variable
    print("a in sample1 :",a)
def sample2():
    print("a in sample2 :",a)
#program execution starts here
sample1()
sample2() #NameError: name 'a' is not defined
print("a in main program :",a) #NameError: name 'a' is not defined
'''
#Global variable
'''
def sample1():
    print("a in sample1 :",a)
def sample2():
    print("a in sample2 :",a)
#program execution starts here
a=45 #global variable
sample1()
sample2() 
print("a in main program :",a) 
'''
#positional arguments
#The number of actual arguments and formal arguments should be same and
# these should be in same order
'''
def sample(a,b,c):
    print(a+b+c)
#program execution starts here
sample(14,87,59,63)#Error
'''
#
'''
def sample(eno,ename,sal):
    print("Eno :",eno)
    print("Ename :",ename)
    print("Sal :",sal)
#program execution starts here
sample(104,"abhi",87465.25)
sample("shimlan",95863.24,109) #Error
'''
#keyword arguments
'''
def sample(eno,ename,sal):
    print("Eno :",eno)
    print("Ename :",ename)
    print("Sal :",sal)
#program execution starts here
sample(104,"abhi",87465.25)
sample(ename="shimlan",sal=95863.24,eno=109)
'''
#default arguments
'''
def sample(a,b=0,c=0,d=0):
    print(a+b+c+d)
#program execution starts here
sample(15,87,49,69)
sample(57,45,96)
sample(45,54)
sample(56)
'''
#
'''
def sample(eno,ename,sal=50000):
    print("Eno :",eno)
    print("Ename :",ename)
    print("Sal :",sal)
#program execution starts here
sample(104,"abhi",87465.25)
sample(105,"shimlan",95863.24)
'''
#variable length arguments
'''
def sample(*args):
    s=0
    for i in args:
        s=s+i
    print("Sum :",s)
#program execution starts here
sample(15,87,49,69,57,96,32,15,16,10,74,43,66)
sample(54,87,96)
'''
#
'''
def sample(cid,cname,*args):
    print("Custid :",cid,end="  ")
    print("Cust name :",cname,end="  ")
    s=0
    for i in args:
        s=s+i
    print("Sum :",s)
#program execution starts here
sample(105,"Yaswanth",15,87,49,69,57,96,32,15,16,10,74,43,66)
sample(106,"Abhishek",54,87,96)
'''
#Keyword variable length arguments
'''
def sample(**kwargs): #kwargs become dict
    for k,v in kwargs.items():
        print(k,":",v)
#program execution starts here
sample(one=111,two=222,three=333,four=444,five=555)
sample(fname="Yaswanth",sname="Ganapathi")
'''
#A function can call another function
'''
def display():
    print("This is display function")
    show() # function call
def show():
    print("This is show function")
#program execution starts here
display() #function call
'''
#recursion -- a function called by itself
'''
def fact(n):
    if(n==0):
        return(1)
    return(n*fact(n-1))
#program execution starts here
n=int(input("Enter a number :"))
f=fact(n)
print("Factorial of %s is %s" %(n,f))
'''
#HW
#lambda function -- Finding a square of a number
'''
s=lambda a:a*a
n=int(input("Enter a number :"))
value=s(n)
print(value)
'''
#Using lambda functions for multiples variables
'''
s=lambda a,b,c:((a*b*c)/10)
value=s(5,7,8)
print(value)
'''
#Using lambda function finding area of circle
'''
s=lambda r:(22/7*(r*r))
r=float (input("Enter a number :"))
value=s(r)
print(value)
'''
