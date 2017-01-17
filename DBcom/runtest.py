import configparser

config = configparser.RawConfigParser()

config.add_section("section1")
config.set("section1", "an_int", "15")
config.set("section1", "a_float", "3.1415")
config.set("section1", "baz", "fun")

# writing our config to one cfg file.
''''
[section1]
an_int = 15
a_float = 3.1415
baz = fun
'''
with open("example.cfg", 'w') as configfile:
    config.write(configfile)



