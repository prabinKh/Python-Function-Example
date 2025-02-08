def addnumber(n):
    return n+2


def process_number(number):
    result = []
    for i in number:
        result.append(addnumber(i))
    return result

numbers = [1,2,3,4,5]
result = process_number(numbers)
print(result)