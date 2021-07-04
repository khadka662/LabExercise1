#Write a function called fizz_buzz that takes a number.If the number is divisible by 3
# it should return “Fizz”.If it is divisible by 5, it should return “Buzz”.
#If it is divisible by both 3 and 5, it should return “FizzBuzz”.Otherwise, it should return the same number.

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
    return str(n)

n=int(input("Enter number:"))

fizzbuzz(n)











