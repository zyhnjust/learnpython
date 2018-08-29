
def fib(max):
    n, a, b=0, 0, 1
    while n < max:
        print b
        a, b= b, a+b
        n = n+1

#print(fib(6))

def fibyield(max):
    n, a, b=0, 0, 1
    while n < max:
        yield b
        a, b= b, a+b
        n = n+1
print fibyield(5)
g=fibyield(6)
for n in g:
    print n
