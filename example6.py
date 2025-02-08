def number(n):
    if n == 0:
        return 'Done'
    else:
        print(n)
        return number(n-1)
    
number(5)