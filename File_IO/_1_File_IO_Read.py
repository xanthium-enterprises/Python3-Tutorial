
PythonText = '''Python is an interpreted high-level general-purpose programming language. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

Python is dynamically-typed and garbage-collected. 
It supports multiple programming paradigms.
Python is often described as a "batteries included" language due to its comprehensive standard library.
Python consistently ranks as one of the most popular programming languages'''

import os

FileObj = open('Python.txt','w')
FileObj.write(PythonText)
FileObj.close()

FileObj = open('Python.txt','r')

print('\n read()-> \n')
print(FileObj.read()) #reads the entire contents to the memory

print('\n readlines()-> \n')
FileObj.seek(0) #goto start of the file
print(FileObj.readlines())#reads the entire contents to the memory in the form of a list

print('\n readline()-> \n')
FileObj.seek(0) #go to start of the file
print(FileObj.readline())# read a single line and stop

FileObj.close()

os.system('dir *.txt')
os.remove('Python.txt')
os.system('dir *.txt')