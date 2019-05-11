import time
import snaps

while True:

    current_time = time.localtime()
    hour_str = str(current_time.tm_hour)
    min_str = str(current_time.tm_min)
    sec_str = str(current_time.tm_sec)


    time_string = hour_str+':'+min_str+':'+sec_str
    snaps.
