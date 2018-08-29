__metaclass__=type # make sure use the new class

class Person:
    def setName(self, name):
        self.name =name
    def getName(self):
        return self.Name
    def greet(self):
        print("Hello world, I'm %s" % self.name) #should be getName?


foo = Person()
bar = Person()
foo.setName("htest1")
bar.setName("htest2")
foo.greet()
bar.greet()
