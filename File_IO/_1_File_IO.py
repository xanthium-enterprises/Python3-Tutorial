#Creating/Opening a file in Python 


FileObj = open('Myfile.txt','w') #open file in read mode
print('FileObj = ', FileObj)

BytesWritten = FileObj.write('Hello from Python\n') #.write() returns the no of bytes written
print('BytesWritten = ',BytesWritten)

StringList = [ 'Hello',' How are You',' 32']
BytesWritten = FileObj.writelines(StringList) #.writelines() writes a List of strings in one go
print('BytesWritten = ',BytesWritten)

open('MyFile2.txt','w').write('hello\n')

FileObj.close() #Close the file 
