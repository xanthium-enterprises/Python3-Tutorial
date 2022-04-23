# My Python Module

ModuleVar = 'Module Variable'

def hello(text):
    print(f'{text} from my_python_module.py')
    
def add(number1,number2):
    return number1 + number2

def multiply(number1,number2):
    return number1 * number2

if __name__ == '__main__':
    print('File is run by itself')
    print(__name__)
else:
    print('File is being Imported')
    print(__name__)