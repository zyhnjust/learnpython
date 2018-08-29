import ConfigParser

#how to read one file
config= ConfigParser.RawConfigParser()
config.read('example.cfg')

a_float=config.getfloat('section1', 'a_float')
an_int = config.getint('section1', 'an_int')

print( a_float + an_int)


#how to user ConfigParser to set value by default
#note, remember () is necessary

config = ConfigParser.ConfigParser()
config.read("example.cfg")

# did not see the differences.
print("sections: ", config.sections())
print( config.options("section1"))
print(config.get('section1', 'a_float', 0))
print(config.get('section1', 'a_float', 1))

