'''
Write a Python program to convert temperatures to and from celsius, fahrenheit.C = (5/9) * (F -32).
'''

temp = input("enter the temperature : ")
degree = int(temp[:-1])
i = temp[-1]
if i.upper() == "C":
  ans = int(round((9 * degree) / 5 + 32))
  o = "Fahrenheit"
elif i.upper() == "F":
  ans = int(round((degree - 32) * 5 / 9))
  o = "Celsius"
print("The temperature in",o, "is", ans, "degrees.")