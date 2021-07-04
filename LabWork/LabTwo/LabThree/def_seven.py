'''
No.7 Write a Python function that accepts a string and
calculate the number of upper case letters and lower case letters.
'''
def upper_lower(string):
    upper_letter = 0
    lower_letter = 0
    for i in string:
        if i.isupper():
            upper_letter+=1
        elif i.islower():
            lower_letter+=1
    print(f'No of upper letters:{upper_letter}')
    print(f'No of lower letters:{lower_letter}')

upper_lower('Hello I am boy')