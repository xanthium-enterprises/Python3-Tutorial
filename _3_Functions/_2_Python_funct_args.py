def function1(a,b,c):
    print(a,b,c)
    
function1(1,2,3)

function1(c=1,b=2,a=3)

function1(1,b=2,c=3)

#function1(a=1,b=2,3) #error

def function2(a=1,b=2,c=3):#default parameter
    print(a,b,c)

function2(5,2,3)
function2(a=100)