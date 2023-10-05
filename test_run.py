from math import *
print("")
s = input("enter equation: y = ")
x = int(input("input x: "))
s = s.replace("^","**")
for i in range(10):
   s = s.replace(f"{i}x",f"{i}*x")

def f(x):
    return eval(s)

print(f(x))