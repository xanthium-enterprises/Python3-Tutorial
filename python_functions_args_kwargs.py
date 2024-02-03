#kwargs - Keyword arguments

def function_1(*args):
    print(args)
    
def function_2(**kwargs):
    print(kwargs)


def function_3(*args,**kwargs):
    print(args)
    print(kwargs)
'''    
function_1(1,2,3,4)
function_2(name ='john',age =28)'''

#function_3(1,2,3,'a','b','c',name ='john',age =28)

a = [1,2,3,'a','b','c']
kw ={'name' :'john','age' :28 }

function_3(a,kw)
function_3(*a,**kw)

