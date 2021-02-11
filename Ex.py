"""
def f(arg1,arg2,arg3 = "Hello"):
    print(arg1,arg2,arg3)
    global x                   //мы не можем использовать переменные
    x = "test1"                //находящиеся внутри функции, но с помощью№ глобал можем
print (x)
f(1,2)
f(1,2,3)
f(arg2 = 15, arg1 =10, arg3 = "test")
"""
   

"""
import random

print(random.randrange(1, 10))
"""

"""                                     //STRING

b = "Hello, World!"
print(b[2:5])


txt = "The best things in life are free!"
print("free" in txt)


b = "Hello, World!"
print(b[-5:-2])

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
"""

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)