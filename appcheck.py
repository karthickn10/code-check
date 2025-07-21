# bad_code.py
import os # ❌ Unused import trends
import sys

class myclass: # ❌ Non-Pascal class name new
    def AddNumbers(self, a, b): # ❌ Wrong function name
        # ❌ Missing function docstring
        temp=a+b # ❌ Inconsistent space
        unused_var = "hello" # ❌ Unused variable
        return temp

def another_func():
    # ❌ Commented-out code
    # if unused_var == "hello":
    #     print("hello")
    print("This is a line that is definitely going to be way too long because we need to test the line length check that is included in pylint which is a very powerful tool for static analysis.") # ❌ Line too long
