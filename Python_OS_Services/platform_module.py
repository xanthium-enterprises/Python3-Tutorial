# Platform module for querying info about your system.
# www.xanthium.in

import platform

print('Generic platform services using platform module')
print('\nOS/Machine info\n')

#Cross platform
print(platform.machine())
print(platform.processor())
print(platform.node())
print(platform.system())
print(platform.release())

print(platform.platform())


#windows
print(platform.win32_ver())
print(platform.win32_edition())
print(platform.win32_is_iot())

#Python
print(platform.python_implementation())
print(platform.python_version())

print(platform.python_build())
print(platform.python_compiler())



