'''
6.Write a Python program to count the number of even and odd numbers from a series of numbers.
'''
numbers=(1,2,3,4,5,6,7,77,44,56,778,899)
even_number = 0
odd_number = 0
for i in numbers:
    if i%2==0:
        even_number += 1
    else:
        odd_number += 1
print(f'No of even numbers:{even_number}')
print(f'No of odd numbers:{odd_number}')