import time

named_tuple = time.localtime() #get the localtime
print(named_tuple)
print(len(named_tuple))
print("\n")

#Format Date and Time

#Week Days
time_string = time.strftime("%a",named_tuple) # %a
print(" Abbreviated weekday name - >",time_string)

time_string = time.strftime("%A",named_tuple)# %A
print("        Full weekday name - >",time_string)

#Date Formats
time_string = time.strftime("%d",named_tuple)# %d
print("        Date               ->",time_string)

#dd/mm/yy format
time_string = time.strftime("%d %B %y ",named_tuple)# 
print("        Date               ->",time_string)

time_string = time.strftime("%d %B %Y ",named_tuple)# 
print("        Date               ->",time_string)

time_string = time.strftime("%d %B %Y ",named_tuple)# 
print("        Date               ->",time_string)

time_string = time.strftime("%d/%B/%Y ",named_tuple)# 
print("        Date               ->",time_string)

#Time Formats

time_string = time.strftime("%H ",named_tuple)# 24 hour clock
print("        Time_Hour_24       ->",time_string)

time_string = time.strftime("%I %p",named_tuple)# 12 hour clock/AM PM indication
print("        Time_Hour_12       ->",time_string)

time_string = time.strftime("%I %p %M min %S sec",named_tuple)# 12 hour clock/AM PM indication
print("        Time_Hour_12       ->",time_string)            # Minutes/Seconds

#Date Time Formats

time_string = time.strftime("%d %B %Y - %Hh %Mmin %Ssec",named_tuple)# 12 hour clock/AM PM indication
print("        Time_Hour_12       ->",time_string)            # Minutes/Seconds
