import threading
import time

exitFlag = 0

class myThread (threading.Thread): #extends from parent
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "existing " + self.name

def print_time(threadName, delay, counter):
    while counter:
#        print "current thread", threading.current_thread()
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print "%s: %s: %d" % (threadName, time.ctime(time.time()), counter)
        counter -= 1
# the last  counter is alwasy 5, so it will be 4321
#
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

#start
thread1.start()
thread2.start()

print "Existing Main thread"







