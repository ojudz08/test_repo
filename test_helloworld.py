"""Test Script for Learning Git Commands
   Created on July 8, 2021
   Author: Ojelle Rogero
   """

def test_print(str):
    text = str
    return text

def add(x, y):
    return x + y

def sub(x, y):
    return x - y
   
def mult(x, y):
    return x * y

print(test_print("Hello World!"))
print("The sum of 10 and 15 is equal to ", add(10, 15))
print("The difference of 10 and 15 is equal to ", sub(10, 15))
print("The product of 10 and 15 is equal to ", mult(10, 15))
