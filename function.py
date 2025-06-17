#Function Topic in python

# def => Define
# Function Name()
# syntax def fun1()
      #statement1
      #statement 2
      #retun

'''
def add(x, y):
    print('Addition of two numbers =>', x + y)

add(5, 10)

def multi(a , b):
    c=a*b
    return c
result=multi(5 ,10)
print('Multiple of two number' , result)
'''
#add two number than calculate the Square of number using function
def add(x1, y1):
    c=x1+y1
    return c

def sqr(z):
    sq=z*z
    return sq

#result=add(5, 10)
answer=sqr(add(5, 10))
print('Square of Sum of the Number=> ' , answer)

#Global Variable=> Global variable can access inside or outside the function...
n=5

def fun2():
    n=2 #Local Variable => Local variable can access only inside the function
    print("Inside the Function => " , n)


fun2()
print("outside the Function => " , n)