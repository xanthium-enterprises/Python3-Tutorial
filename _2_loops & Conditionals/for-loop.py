#for loop

Number1 =[2,4,6,8]
Number2 =[0,0,0,0]
count = 0
for No in Number1:
    Number2[count] = No*2
    #print(Number2[count])
    count+=1

print('Number1 [] ->',Number1)
print('Number2 [] ->',Number2)

print('\n')

character = ["Spam","Mangos","Apple","Pie"]
for x in character:
    #print(x,end = ' ')
    print(x,end = '-')
    #print(x,end = '+')
    
S= "Hello,How are you"
for x in S:
    print(x)