import datetime
import time

frame_rate = 1 # fps

prev_time = time.time()
try:
    while True:
        if (time.time()-prev_time) > frame_rate:
            prev_time = time.time()
            print(time.time())
except KeyboardInterrupt:
    print('terminate')


iso_date = datetime.datetime.now().isoformat()
nano_time = time.time()

iso_date
nano_time

ts = time.time()
ts = time.strftime()
ts
time.sleep(60)
print(time.time()-ts)