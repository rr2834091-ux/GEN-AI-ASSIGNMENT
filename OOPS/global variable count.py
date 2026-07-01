print('Global Variable')
count=2000
class Demo:
    def update(self):
        global count 
        count=10000
obj = Demo()
obj.update()
print('Global count:',count)
        
