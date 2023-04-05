import hashlib
import time

start_time = time.perf_counter()
str = "俺打算，但那索伦蒂诺撒离开你打算aasadas"
hashlib.sha1(str.encode("utf8")).hexdigest()
end_time = time.perf_counter()
total_time = end_time-start_time
print(total_time*1000)
