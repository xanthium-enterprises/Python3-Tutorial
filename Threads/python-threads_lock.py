'''
Program to demonstrate locks in Python threading

'''

import time
import threading


def update_list_A(var_list):
    print('update_list_A thread called ')
    #lock.acquire()
    for _ in range(10):
        var_list.append('A')
        time.sleep(0.10)
    
    #lock.release()
    
        
    
def update_list_B(var_list):
    print('update_list_B thread called ')
    #lock.acquire()
    for _ in range(10):
        var_list.append('B')
        time.sleep(0.10)
    #lock.release()

lock = threading.Lock()

shared_list =[] #Shared variable to be modified in threads


t1 = threading.Thread(target = update_list_A, args = (shared_list,))
t2 = threading.Thread(target = update_list_B, args = (shared_list,))


t1.start()
t2.start()


t1.join()
t2.join()

print(shared_list)
print('End of Main Thread')


