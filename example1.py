"""
The iner function shund return the string
, and the outter function  should the value received from
innerfunction . 
 bug in the code that cause it to fail

"""

def inner_function():
    return "Hello, World!"

def outter_function():
    resultss= inner_function()
    return resultss

result = outter_function()
print(result)