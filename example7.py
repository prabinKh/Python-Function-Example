def apply(func,list_name=None):
    if list_name is None:
        list_name= []
    list_name.append(func)

    return list_name

print(apply(0))