# FileIO using Exceptions

try:
    with open('Data.txt','w') as FileObj:
        FileObj.write('Hello')
    
except Exception as value:
    print(f'An Exception -> {value} occured')
    
else:
    print('No Exception Occured ')
    


