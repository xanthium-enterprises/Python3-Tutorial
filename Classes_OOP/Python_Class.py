# Python Classes



class MyClass:
    
    MyClassVar = 89; # static variables
    
    def __init__(self,value):
        print('Constructor Called')
        self.value = value
    
    def greetings_s():   #static Method 
        print("hello from MyClass - static method calling")
        
    def greetings(self):# instance method, self
        print("hello from MyClass - Instance Method()")
    
    ''' No function overloading in Python

    def greetings(self,name):
        print(f'hello from {name} - Instance Method()')
    '''       
    

MyClass.greetings_s() #static class method calling        
print(f'Static Variable = {MyClass.MyClassVar}')        
MyClassInst1 = MyClass(2)

MyClassInst1.greetings()

print(MyClassInst1.value)