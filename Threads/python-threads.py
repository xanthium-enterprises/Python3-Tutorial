import time
import threading


def do_something(delay=1):
    print(f'Start Sleeping for {delay} second')
    time.sleep(delay)
    print('Done Sleeping')

start_time = time.perf_counter()

t1 = threading.Thread(target = do_something,args =(4,))
t2 = threading.Thread(target = do_something,args =(4,))

t1.start() #start the  threads
t2.start()

#t1.join()
#t2.join()

stop_time = time.perf_counter()

print(f'Time Elapsed {round(stop_time-start_time,3)} Seconds\n') #round(value,no of decimal places)




