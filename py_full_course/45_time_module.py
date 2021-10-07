import time

print(time.ctime(0)) # epoch time
print(time.time()) # return current seconds since epoch

print(time.ctime(time.time())) # current time

time_object = time.localtime()
formatted_time = time.strftime("%B %d %Y %H:%M:%S", time_object) # %_ larning vazifalarini dokumentatsiyadan ko'rish mumkin
print(formatted_time)

time_object = time.gmtime() # UTC time

time_string = "12 May 2001"
time_object = time.strptime(time_string, "%d %B %Y") # time.strptime() time object qaytaradi
print(time_object)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)