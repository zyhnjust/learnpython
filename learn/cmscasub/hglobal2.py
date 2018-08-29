
x=50

def func(x):
#    global x
    print "inner x=", x
    x=30
    print "inner x=", x

func(x)
print "outer x : ", x
x=60
func(x)