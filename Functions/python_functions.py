# Python Functions

def positional_args(arg1,arg2,arg3):
    print(f'arg1 = {arg1}')
    print(f'arg2 = {arg2}')
    print(f'arg3 = {arg3}')
    
    L = []
    L.append(arg1)
    L.append(arg2)
    L.append(arg3)
    
    return L

    
def keyword_args(arg1,arg2,arg3):
    print(f'arg1 = {arg1}')
    print(f'arg2 = {arg2}')
    print(f'arg3 = {arg3}')
    
def default_args(arg1,arg2='default',arg3='default'):
    print(f'arg1 = {arg1}')
    print(f'arg2 = {arg2}')
    print(f'arg3 = {arg3}')    
'''    
return_value = positional_args('r',2,3)
print(f'return value ={return_value}')

keyword_args(arg1=1,arg2=3,arg3=4)
print()
keyword_args(arg2=1.897,arg1=31.8689,arg3=4.987)

'''
default_args(1)
print()
default_args(1,2,3)

