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

for Line in FileObj:
    print(Line)