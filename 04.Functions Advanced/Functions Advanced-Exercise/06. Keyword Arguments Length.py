def kwargs_length(**kwargs):
    return len(kwargs)


print(kwargs_length(**{'name' : 'stefi', 'age' : '21'}))