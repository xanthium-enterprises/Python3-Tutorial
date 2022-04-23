#Functions in Python

def hello():
    print("Hello 'World'  ")
    

x = hello # asign hello to x 
y = hello # asign hello to y


x()
y()



def list_change(listvar):
    listvar[0] = 'Changed'
    
L =['Hello','How',1,4,2.34]

print(f'Before Change =  {L}')
list_change(L)
print(f'After Change  =  {L}')


