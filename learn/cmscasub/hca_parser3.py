from optparse import OptionParser


parser = OptionParser()

parser.add_option("-f", "--file",
                  action="store", type="string", dest="filename")
parser.add_option("-p", "--1file",
                  action="store", type="string", dest="filename1")

args = ["-f", "foo.txt"]
(options, args) = parser.parse_args(args)
print options.filename, args
# print options["-f"]


args1 = ["-p", "foo1111.txt"]
(options1, args1) = parser.parse_args(args1)
print options1.filename1

args2 = ["--1file", "foo11111122222.txt"]
(options1, args2) = parser.parse_args(args2)
print options1.filename1
