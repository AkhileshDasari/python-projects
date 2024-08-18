import time

#secs = int(input("enter seconds: "))
#minute = int(input("enter minutes: "))
#hours = int(input("enter hours: "))

time_ = int(input("enter time in seconds: "))
for x in reversed(range(1 , time_ + 1)):
    seconds = int(x % 60)
    minute = int(x / 60) % 60
    hour = int(x / 3600) 
    print(f"{hour:02}-{minute:02}-{seconds:02}")
    time.sleep(1)
print("its time!!")
