
# FORMATION PYTHON

# 1.0 Comments and print() statement

# This is a comment. THerefore, it is not going to be executed

"""
This is a way to make several line comments



print("Hello world")

"""

# 2.0 Variables and simple data types

"""
a = "This is a variable that represents a string"

b = 1 # int

print(type(b))

c = 1.5 # float

print(type(c))

d = True # bool

print(type(d))

e = False # bool

print(type(e))

print(c)

"""

# 2.1 String concatenation
"""

a = "Hello"

b = "World"

c = a + b

print(c)

print(a + " " + b)

# 2.2 f-strings

name = "Alba"

height = 175

fstring = f"{name} has a height of: {height} cm"

print(fstring)

# 2.2 String methods

a = "nombre apellido edad"

b = a.split(" ")

print(b)


"""

# 3.0 Complex data types
"""
# 3.1 List

a = [1,2,3,4,5,"a", "b", "c"]

print(a)

# 3.1.1 Accessing elements

print(a[0],a[-1])

# 3.1.2 Slicing

b = a[1:5]

print(b)

# 3.1.3 Lenght

dim = len(a)

print(dim)

# 3.1.4 String methods

list = []

list.append("elemento añadido")

print(list)

list.pop()

print(list)
"""
# 3.2 Tuples

# def and accessing

# 3.3 Dictionaries
"""
dict = {
        "name": "Jaime",
        "age": 28,
        "studies": "engineer"}

print(dict)

# 3.3.1 accessing

name = dict["name"]

print(name, dict["age"])

# 3.3.2 list inside dictionaries

dict1 = {
    "name": ["jaime","pablo"],
             "age": [28,50]}

print(dict1)
"""
# 3.4 Flow Control 
# 3.4.1 Conditionals
"""
altura = 160

if (altura >= 175):
    
    print("eres una persona alta")
else:
    print("no eres una persona alta")
    """
# 3.4.2 Loops
"""
a = ["a","b","c","d"]

for i in a:
    if(i =="b"):
        continue
    if(i =="c"):
       
        break
    
    print(i)
    
rangevar = range(5)
print(rangevar)

for i in range(len(a)):
    print(a[i])
    
  """

# 3.6 Functions
"""
def sumar(num_1, num_2):
    
    result = num_1 + num_2
    
    return result

suma = sumar(5,9)

print(suma)

"""
# 3.7 Documents

# 3.7.1 Write

f = open("test.txt", "w") # w - overwrite, a - append, r - read
"""
f.write("Hola, como estais")
f.write("\nmi nombre es Jaime,")
f.write("\ntrabajo en WTW")

f.close()

"""
# 3.7.2 Read

"""
f = open("test.txt")

a = f.readlines()

print(a)

for i in a:
    
    print(i)
    
f.close()

"""

# 3.8 Modules

import pandas as np

# if package is not installed -> anaconda prompt - pip install name_module

# then, in the code -> import name_module as whatever

# functions of the module can be used like this -> whatever.funcion_Del_modulo



    
