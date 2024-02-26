import time
import threading  

def append_list_thread():
   global_list.append('Appended in append_list_thread()')


   
global_list = [] #Create empty global list



global_list.append('Appended in Main Thread')

print(global_list) #before calling the thread

t1 = threading.Thread(target = append_list_thread)
t1.start()
t1.join()



print(global_list) #after calling the thread