'''' import time
import threading


def do_something():
    print('Start Sleeping')
    time.sleep(1)
    print('Done Sleeping')

start_time = time.perf_counter()
do_something()
stop_time = time.perf_counter()

print(f'Time Elapsed {round(stop_time-start_time,4)} Seconds') '''



for x in range(8):
    print(f'{x}->p')

