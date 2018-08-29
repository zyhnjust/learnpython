
import time

ticks = time.time()
print "current time is ", ticks

localtime = time.localtime(ticks)
print "current localtime is ", localtime

localasctime = time.asctime( time.localtime(time.time()) )
print "current localasctime is ", localasctime

strTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print "current strTime is ", strTime

# convert from string to long back
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
