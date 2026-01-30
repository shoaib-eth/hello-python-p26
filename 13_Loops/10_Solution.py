import time

wait_time = 1 # In seconds
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    print("Attempts: ", attempts + 1, "-wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1