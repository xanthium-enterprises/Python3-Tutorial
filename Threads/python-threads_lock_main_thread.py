import time
import threading


def function_t(): 
    lock.acquire()
    
    print('\nfunction_t entered')
    time.sleep(5)
    print('function_t exited')
    
    lock.release()
    

lock = threading.Lock() #create the lock object

t1 = threading.Thread(target = function_t)

print( 'locking main thread for  seconds')
lock.acquire() #acquire the lock in main thread and never release preventing  
               # t1 from ever running
t1.start()
time.sleep(10)  # or release after 5 seconds             
#lock.release()
print( 'lock released after 5 seconds')


t1.join()

print('End of Main Thread')


