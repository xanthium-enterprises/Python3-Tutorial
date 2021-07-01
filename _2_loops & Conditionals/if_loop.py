#if/else/elif Conditionals

input_data = input('enter a number ->')

if input_data.isdigit() == True:
    print('Number is a Digit')
    print('You entered ->',input_data)
    print()
else:
    print('Number is not a Digit')
    print('You entered ->',input_data)
    print()
    
print('Fin')
print('=' * 20)