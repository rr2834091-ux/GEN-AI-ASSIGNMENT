#Area of the Rectangle Data abstraction:
from abc import ABC,abstractmethod
class shape(ABC):
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print('area=',self.length*self.width)
r=rectangle(5,5)
r.area()
        
