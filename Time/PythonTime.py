
import time

print(time.gmtime(0)) #Start of epoch

Sepoch = Seconds_elapsed_since_Epoch = time.time()

print('Seconds_elapsed_since_Epoch ->',Seconds_elapsed_since_Epoch)

print('Time Human Readable ->', time.ctime(Sepoch))
print ('Time Human Readable ->', time.ctime())

L = time.gmtime()
print(L)
print(L[0])
print(L[1])
print(L[2])
print(L[3])
print(L[4])