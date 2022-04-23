# Exceptions in Python

No = input('enter a number - ')
No =int(No)

try:
    Output = 100/No
    print('Output = ',Output)

except:
    print('An Exception Occured')
    
    
else:
    print('No,Exception occured so We are in else: block')
    
finally:
    print('We are in finally:')
    
print('--------End----------')
    
    
