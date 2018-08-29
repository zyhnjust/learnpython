class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def setSize(self, size):
        self.width=size
        self.height=size
    def getSize(self):
        return self.width, self.height
r=Rectangle()
print(r.width)
print(r.height)
print(r.getSize())
r.setSize(100)
print(r.width)
print(r.size)
