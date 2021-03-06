#!/usr/bin/env python3
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
	def __init__(self, threadId, name, counter):
		threading.Thread.__init__(self)
		self.threadId = threadId,
		self.name = name
		self.counter = counter
		
	def run(self):
		print ("开始线程：" + self.name)
		threadlock.acquire()
		print_time(self.name, self.counter, 5)
		print ("退出线程：" + self.name)
		threadlock.release()
		
def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadlock = threading.Lock()

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")