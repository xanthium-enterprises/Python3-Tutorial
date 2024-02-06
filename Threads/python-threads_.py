import time
import threading


def change_var_list1(var_list):
    print('change_var_list1')
    lock.acquire()
    for _ in range(10):
        var_list.append('A')
        #time.sleep(0.10)
    print(shared_var_list)
    lock.release()
    
        
    
def change_var_list2(var_list):
    print('change_var_list2')
    lock.acquire()
    for _ in range(10):
        var_list.append('B')
        #time.sleep(0.10)
    lock.release()

lock = threading.Lock()

shared_var_list =[] #Shared variable to be modified in threads

t2 = threading.Thread(target = change_var_list2, args = (shared_var_list,))
t1 = threading.Thread(target = change_var_list1, args = (shared_var_list,))



t2.start()
t1.start()
t1.join()
t2.join()

print(shared_var_list)


