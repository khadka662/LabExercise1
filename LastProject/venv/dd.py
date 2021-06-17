
def Add():
    a=int(input('enter the first value:'))
    b= int(input('enter the second value:'))
    c=a+b
    print(f'the sum of {a} and {b} is {c}')

def sub(a,b):
    c= a-b
    print(f'the subraction of {a} and {b} is {c}')

def mul():
    a = int(input('enter the first value:'))
    b = int(input('enter the second value:'))
    c = a * b
    return c

def div(a,b):
    c= a/b
    return c
div(4,2)




def add():
    a=int(input("enter the first number"))
    b=int(input("enter the number "))
    c=a+b
    print(f"sum of number is ",c)
def sub(a,b):
    c = a-b
    print(f"defference of number is ", c)
def mul():
    a=int(input("enter the first number"))
    b=int(input("enter the number "))
    c=a*b
    return c
def divide(a,b):

    d=a/b
    return d
add()
sub(5,3)
c=mul()
print(f"multiplication of the numbers is",c)
d=divide(6,3)
print(f"division of the numbers is",d)

def add():#fumctions : no parameter and no return statement
    a= int(input('enter the value a:'))
    b=int(input('enter the value b:'))
    c=a+b
    print(f'the sum of {a} and {b} is {c}')
add(2,4)

def sub(a,b):#function =parameter and no return statement
    c=a+b
    print(f'the subraction of {a} and {b} is {c}')
sub(6,2)

def mul():#function =no parameter and return statement
    a = int(input('enter the value a:'))
    b = int(input('enter the value b:'))
    c=a*b
    return c
mul(3,2)

def div(a,b):# parameter and return statement
    c = a / b
    return c
div(4,2)

#add
def add():
    a = int(input("Emter the value of a:"))
    b = int(input("Emter the value of b:"))
    c = a+b
    print(f"the sum of {a} and {b} is {c}:")
add()


#sub
def sub(a,b):
    c= a - b
    print(f"the diff of {a} and {b} is {c}:")
sub(5,3)

#multiply
def mul():
    a = int(input("Emter the value of a:"))
    b = int(input("Emter the value of b:"))
    c = a*b
    print(f"the multiplication  of {a} and {b} is {c}:")
    return c
mul()

#divide
def div(a,b):
    c= a//b
    print(f"the division of {a} and {b} is {c}:")
    return c
div(18, 3 )

