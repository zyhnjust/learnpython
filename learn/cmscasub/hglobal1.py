

#global usage
'''
自己觉得 如果用global 里面直接可以修改外的值。
如果另外一种方式就是说参数导入， 是只能修改局部变量的。
check global2.py
'''
x=50

def func():
    global x
    print "inner x=", x
    x=30
    print "inner x=", x

func()
print "outer x : ", x
x=60
func()

###############

