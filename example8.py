"""
1. first function to calculate the sum of two numbers
2. second function to calculate the differece of two numbers
3. third function to calculat the product of two numbers
"""

def sum_of_two_numbers(a,b):
    return a+b

def difference_of_two_numbers(a,b):
    return a - b

def product_of_two_numbers(a,b):
    return a * b

def devision_of_two_numbers(a,b):
    if b ==0:
        return "Error: Division by zero is not allowed."
    return a / b


def __main__(a,b):
    sum_result = sum_of_two_numbers(a, b)
    difference_result = difference_of_two_numbers(a, b)
    product_result = product_of_two_numbers(a, b)
    devision_result = devision_of_two_numbers(a, b)

    # return sum_result, difference_result, product_result, devision_result


if __name__== "__main__":
    first = int(input('first number : '))
    second = int(input('second number : '))

    final_result = __main__(first,second)
    print(final_result)

