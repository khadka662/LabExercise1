
def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print('This is my sample application')
print('******************')
print('program start:')
while True:
    print('Menu:\n1. add\n2. sub\n3. mul\n4. div')
    option=int(input('Choose your option:'))
    print('*******************')
    first=float(input('Enter first value:'))
    second=float(input('Enter second value:'))
    if option==1:
        answer=add(first,second)
        print(f'The result is {answer}​​')
    elif option==2:
        answer=sub(first,second)
        print(f'The result is {answer}​​')
    elif option==3:
        answer=mul(first,second)
        print(f'The result is {answer}​​')
    elif option==4:
        answer=div(first,second)
        print(f'The result is {answer}​​')
    else:
        print('please insert valid option')

    choice=input('Do you want to continue-(y/n)')
    if choice=='n':
        print('Thank you --')
        break


