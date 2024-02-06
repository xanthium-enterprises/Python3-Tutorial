''' Shared Memory between threads and main thread of execution'''


import time
import threading

#doubles the member of the list passed to it 
def double_list(integer_list):
    
    for i in range(len(integer_list)):
        integer_list[i] = integer_list[i]*2
        

def double_int(int_var):
    int_var = int_var*2
    print(f'ivar inside thread --> {int_var}')
        
ilist =[1,2,3,4,5] #original list
ivar = 5           #integer to double in thread

print('Original List    -> ',ilist)
print('Original Integer -> ',ivar)

double_list_thread = threading.Thread(target = double_list,args=(ilist,)) #original list send to thread for doubling
double_list_thread.start()


int_thread = threading.Thread(target = double_int,args=(ivar,)) #original integer send to thread for doubling
int_thread.start()

double_list_thread.join()
int_thread.join()

print('\n\nUpdated List     -> ',ilist)#updated data from thread reflected in the original ilist
print('Updated Integer  -> ',ivar)

