'''
9.Write a program to find the factorial of a number.
'''
def factorial(num):
    fact=1
    for i in range(2,num+1):
        fact=fact*i
    print(f'factorial of {num} is {fact}')
num=int(input('enter the number'))
factorial(num)