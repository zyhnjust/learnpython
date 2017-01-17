def hello(var):
    'test hello'
    1+1
    var = "newValue"
    print("internal value: " + var)
    return 'hello'


value = 'old value'
hello(value)
print("out value:" + value)

#print(hello.__doc__)
#help(hello)

def hello_3(greeting="hello", name="world"):
    print ('%s, %s!' % (greeting, name))

hello_3()
hello_3('Greetings', name='universe')
