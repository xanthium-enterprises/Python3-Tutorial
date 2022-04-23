#using Signals in Python 3.x.x

#Signals.SIGINT:  CTRL + C ,Default action is to raise KeyboardInterrupt.
#Signals.SIGTERM: Termination signal.
#Signals.SIGBREAK:Interrupt from keyboard (CTRL + BREAK).
 

import signal # Import signal module using the import keyword
import time   # available signals on your system

# available signals on our System
valid_signals = signal.valid_signals()     # requires python 3.9.0
print('available Signals ->',valid_signals)

# Create a Signal Handler for Signals.SIGINT:  CTRL + C 
def SignalHandler_SIGINT(SignalNumber,Frame):
	print('SignalHandler of signal.SIGINT')
	print(f'Signal Number -> {SignalNumber} Frame -> {Frame}')
    
#create a Signal Handler for Signals.SIGBREAK:(CTRL + BREAK)
def SignalHandler_SIGBREAK(SignalNumber,Frame):
	print('SignalHandler of signal.SIGBREAK')
	print(f'Signal Number -> {SignalNumber} Frame -> {Frame} ')
        
signal.signal(signal.SIGINT,SignalHandler_SIGINT)
signal.signal(signal.SIGBREAK,SignalHandler_SIGBREAK)


while 1:  
    print("Press Ctrl + C ") 
    time.sleep(1) 