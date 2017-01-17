
def print_params(*params):
    print (params)

(print_params('Testing'))
(print_params(1,2,3))
(print_params('Testing'))

#Verify multiple params
def print_params2(title, *params):
    print(title)
    print(params)
print_params2('testing: ', 1,2,3)

#how to collect dictionary
def print_params3(title, **params):
    print(title)
    print(params)

print_params3("testing dic: ", param1=12, param2=13)

