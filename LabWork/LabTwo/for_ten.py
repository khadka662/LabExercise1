# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
def num(x,y,z):
    if x==y or y==z or x==z:
        sum=0
    else:
        sum=x+y+z
    return sum
print(num(1,2,3))
print(num(2,2,6))






