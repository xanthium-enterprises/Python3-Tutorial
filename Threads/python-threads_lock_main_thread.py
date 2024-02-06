import time
import threading


def function_t(): 
    
    tl = lock.acquire(timeout = 10 )
    print(tl)
    
    
    lock.release()
    

lock = threading.Lock() #create the lock object

t1 = threading.Thread(target = function_t)

print( 'locking main thread forever')
l= lock.acquire() #acquire the lock in main thread and never release preventing  
               # t1 from ever running
t1.start()

print( 'lock status =',l)


t1.join()


print('End of Main Thread')


