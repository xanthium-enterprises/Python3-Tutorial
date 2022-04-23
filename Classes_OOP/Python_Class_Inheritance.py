'''
Python  Inheritance

'''

class MySuperClass():
    def greeting(self):
        print('Message from Super class')
        
class MySubClass(MySuperClass):
    def greeting(self):
        print('Message from Sub class')
        MySuperClass.greeting(self)
        
SC   = MySuperClass()
SubC = MySubClass()

SC.greeting()
SubC.greeting()