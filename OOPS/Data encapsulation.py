class Mobile:
    def __init__(self,brand,pin):
       self.brand=brand
       self.pin=pin
    def Change_pin(self,old_pin,new_pin):
        if old_pin == self.pin:
           self_pin=new_pin
           print('PIN changed succesfully.')
        else:
           print('Incorrect old PIN.')
    def verify_pin(self,pin):
        if pin==self.pin:
            print('PIN verified.')
        else:
            print('Invalid PIN.')
phone=Mobile('MOTO',1615)
print('Mobile Brand :',phone.brand)

phone.verify_pin(1615)
phone.Change_pin(1615,3015)
phone.verify_pin(1615)
