# using the with statement

with open('Myfile.txt','w') as FileObj:
    FileObj.write('Hello\n')
    FileObj.write('Hello how are you\n')
    print('FileObj.mode ->',FileObj.mode)
    print('FileObj.name ->',FileObj.name)
    print('FileObj.closed ->',FileObj.closed)
    print(FileObj)
    
print('\nFileObj.closed ->',FileObj.closed)