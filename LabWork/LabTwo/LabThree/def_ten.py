'''
Write a python program to check whether the number is Armstrong number or not using function:
[Hint: 153 - 1*1*1 + 5*5*5 + 3*3*3]
'''
def armstrong(num):
    i =num
    sum=0
    while (i!=0):
        r = i % 10
        sum += r ** 3
        i = i // 10
    if num==sum:
         print(num,'is armstrong number')
    else:
         print(num,'is not armstrong number')

    return(sum==num)
num=int(input('enter the number:'))
armstrong(num)