class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
#    def setSize(self, size):
#        self.width=size
#        self.height=size
#    def getSize(self):
#        return self.width, self.height
#    size=property(getSize, setSize)
    def __setattr__(self, key, value):
        if key == 'size':
            self.width, self.height=value
        else:
            self.__dict__[key]=value
    def __getattr__(self, item):
        if item == 'name':
            return self.width, self.height
        else:
            raise AttributeError

r=Rectangle()
print(r.width)
print(r.height)
print(r.getSize())
r.setSize(100)
print(r.width)
print(r.size)

