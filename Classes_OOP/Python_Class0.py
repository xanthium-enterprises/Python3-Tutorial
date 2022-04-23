
class Dog:
    
    attr1 = 'mammal'  # Class Variables
    attr2 = 'dog'     # Class
    
    def __init__(self,name,colour): #constructor
        self.name   = name #instance variables
        self.colour = colour
    
    
x = Dog('steven','red')
y = Dog('hawkings','purple')

print(x.name,x.colour)
print(y.name,y.colour)

print(Dog.attr1)