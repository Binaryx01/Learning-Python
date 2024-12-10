#Write a program to convert Celsius to Fahrenheit.

"""
180c = 100(f-32)
18c=10(f-32)
9c=5(f-32)
c = 5/9(f-32)
"""

c = int(input("enter the celsius"))
f = (9 / 5) * c + 32
print(f)

