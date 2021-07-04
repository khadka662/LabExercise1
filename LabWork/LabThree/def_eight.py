'''
Q.No.8 Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and
that has no positive divisors other than 1 and itself.
'''
def prime_num(number):
        for i in range(2,number):
            if(number%i)==0 and i>1:
                print(f'{number} is  not prime number')
                break
            else:
                print(f' {number} is prime number')
                break
number=int(input('enter the number:'))
prime_num(number)