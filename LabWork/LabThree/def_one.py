
'''

1 Write a Python function to find the Max of three numbersQ.
No
2. Write a function calledfizz_buzzthat takes a number.If the number is divisible by
3, it should return “Fizz”.If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.Otherwise, it should return the same number.
3. Write a function calleds how Numbers that takes a parameter called limit.
It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
For example, if the limit is 3, it should print:0 EVEN1 ODD2 EVENQ.
4. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit(parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20Q.
5. Write a function calleds how_stars(rows).If rows is 5, it should print the following:***************Q.
No.6 Write a Python program to reverse a string.Q
No.7 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Q.No.8 Write a Python function that takes a number as a parameter and check the number is prime or not.Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.Q.No.
9 Write a Python function that checks whether a passed string is palindrome or not.'''

num1 = int(input('enter first number:'))
num2 = int(input('enter second number:'))
num3 = int(input('enter third number:'))
def q(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(f'{num1} is largest')
    elif num2>num1 and num2>num3 :
        print(f'{num2} is largest')
    else:
        print(f'{num3} is largest')
q(num1 ,num2,num3)
