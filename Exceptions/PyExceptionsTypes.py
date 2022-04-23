# Exceptions in Python

No = input('enter a number - ')
No =int(No)

try:
    Output = 100/No
    print('Output = ',Output)

except ArithmeticError:
    print('An ArithmeticError Exception Occured,Eg divide by zero')
    
except TypeError as value:
    print('A TypeError Exception Occured')
    print('value =',value)
    
except:
    print('Any Exception Occured')
    
else:
    print('No,Exception occured so We are in else: block')
    
finally:
    print('We are in finally:')
    
print('--------End----------')
    
    

