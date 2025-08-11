import time
from time import sleep

Seconds = int(input("Enter Number of Seconds : "))

for x in range(Seconds , 0 , -1):
    s = x%60
    m = int(x/60)%60
    h = int(x/3600)

    print(f"{h:02}:{m:02}:{s:02}")
    sleep(1)

print("WAKE UPPPPP")
