#!/usr/bin/env python3
import _thread
import time

def print_time(threadName, delay):
	count = 0
	while (count < 5):
		time.sleep(delay)
		count += 1
		print("%s: %s" % ( threadName, time.ctime(time.time()) ))
		
try:
	_thread.start_new_thread(print_time, ("Thread-1", 2, ))
	_thread.start_new_thread(print_time, ("Thread-2", 4, ))
except Exception as e:
	print("Error: can not start the thread", e)

while 1:
	pass