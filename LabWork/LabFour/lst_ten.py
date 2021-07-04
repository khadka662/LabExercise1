'''
Write a Python program that accepts a string and calculate the number of digits and letters
'''
s = input("Input a string:")
digit=0
letter=0
for i in s:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        letter=letter+1
    else:
        pass
print("Letters", letter)
print("Digits", digit)


