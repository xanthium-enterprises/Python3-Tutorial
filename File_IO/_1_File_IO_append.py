# append to a file

import os

FileObj = open('Python.txt','w') # create a file
FileObj.write('This is the first line \n')
FileObj.write('This is the Second line \n')
FileObj.close()
FileObj = open('Python.txt','a') #append new data
FileObj.write('This is the appended line \n')
FileObj.write(r'This is the raw string line \n')# raw string \n is written 
FileObj.close()

