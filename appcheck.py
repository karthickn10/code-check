import os
import math
import random  # unused

# def unused_func():
#     print("This function is commented out")

def AddNumbers(a,b):  # Wrong naming + no type annotations
    temp = a+b  # No spaces
    result = temp + 5
    temp2 = 100  # unused variable
    return result

def another_function():
	print("This line is tab-indented")  # tab used
	print("Another line") 

if False:
    print("This block will never run")

class myclass:  # class name not in PascalCase
    def __init__(self):
        self.Value=10  # bad spacing and casing

def long_line():
    print("This is a very long line that definitely exceeds one hundred characters for sure, which breaks style guides.")

def unused_args(x, y, z):  # z is unused
    return x + y
