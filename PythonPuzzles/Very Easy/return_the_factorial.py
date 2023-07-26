"""
Create a function that takes an integer and returns the factorial of that integer.
That is, the integer multiplied by all positive lower integers
"""
def factorial(num):
    counter = num - 1
    while counter > 1:
        num *= counter
        counter -= 1
    return num 
    
print(factorial(2))