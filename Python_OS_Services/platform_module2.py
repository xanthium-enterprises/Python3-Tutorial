# Platform module for querying info about your system.
# www.xanthium.in

import platform

print('Generic platform services using platform module')
print('\nOS/Machine info\n')

#Cross platform
print('\n----------------------------------------------------')
print('\nCross platform OS ')
print('\n----------------------------------------------------')
print('Machine Type   -> ' + platform.machine())    #returns the machine type Eg i386 or AMD64
print('Processor Name -> ' + platform.processor())  #returns the real processor name
print('OS name        -> ' + platform.system())     #returns the OS name Eg Windows,Linux,Java,Darwin
print('OS Release No  -> ' + platform.release())    #returns the OS release number

print('\nOS full name   -> ' + platform.system() +'-' +platform.release())

print('\nNetwork Name   -> ' + platform.node())       #returns the computers network name


#Python

print('\nPython Environment ')
print('\n----------------------------------------------------')
print('\nPython Implementation  -> ' + platform.python_implementation()) # which type of Python implementation.Eg‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.print(platform.python_version())
print('Python version         -> ' + platform.python_version()) #version of the installed python

#Returns a tuple (buildno, builddate) stating the Python build number and date as strings
BuildNumberTuple = platform.python_build() 

print('Python build Number    -> ' + BuildNumberTuple[0])
print('Python build Date      -> ' + BuildNumberTuple[1])  
print('Compiler used to build -> ' + platform.python_compiler()) #Returns a string identifying the compiler used for compiling Python



#windows specific
print('\n----------------------------------------------------')
print('\nWindows Specific')
print('\n----------------------------------------------------')
Win32_Version_Tuple = platform.win32_ver()

print('Windows OS Release       -> ' + Win32_Version_Tuple[0])
print('Windows OS Version       -> ' + Win32_Version_Tuple[1])
print('CSD level (service pack) -> ' + Win32_Version_Tuple[2])
print('Windows OS type          -> ' + Win32_Version_Tuple[3])

print('Windows Current Edition  -> ' + platform.win32_edition()) #string representing the current Windows edition
#CoreSingleLanguage -only 1 language ,other language packs need to be installed
print('Is Platform Windows IOT  -> ' + str(platform.win32_is_iot())) # is platform a windows iot,return bool






