def ratrow():
    f=open('pattern.txt','w+')
    f.write('RIGHT ANGLE TRAINGLE NUMBER ROW\n.....................\n')
    for i in range(1,6):
        for j in range(0,i):
         f.write(str(i))
        f.write('\n')
    f.close()
        
ratrow()


def ratrow():
    f=open('pattern.txt','a+')
    f.write('RIGHT ANGLE TRAINGLE NUMBER COL\n.....................\n')
    for i in range(1,7):
        for j in range(1,i):
         f.write(str(j))
        f.write('\n')
    f.close()
        
ratrow()

def RATSTAR():
    f=open('pattern.txt','a+')
    f.write('RIGHT ANGLE TRAINGLE NUMBER STAR\n.....................\n')
    for i in range(1,6):
        for j in range(0,i):
         f.write(('*'))
        f.write('\n')
    f.close()
RATSTAR()

def RATnameup():
    f=open('pattern.txt','a+')
    f.write('RIGHT ANGLE TRAINGLE NAME UPPER ROW\n.....................\n')
    for i in range(1,6):
        for j in range(0,i):
         f.write(chr(i+64))
        f.write('\n')
    f.close()
RATnameup()

def RATnameup():
    f=open('pattern.txt','a+')
    f.write('RIGHT ANGLE TRAINGLE NAME UPPER COL\n.....................\n')
    for i in range(1,6):
        for j in range(0,i):
         f.write(chr(j+65))
        f.write('\n')
    f.close()
RATnameup()

def RATnamelow():
    f=open('pattern.txt','a+')
    f.write('RIGHT ANGLE TRAINGLE NAME LOWER ROW\n.....................\n')
    for i in range(1,6):
        for j in range(0,i):
         f.write(chr(i+96))
        f.write('\n')
    f.close()
RATnamelow()


def RATnamelow():
    f=open('pattern.txt','a+')
    f.write('RIGHT ANGLE TRAINGLE NAME LOWER COL\n.....................\n')
    for i in range(1,6):
        for j in range(0,i):
         f.write(chr(j+97))
        f.write('\n')
    f.close()
RATnamelow()

def ILATrow():
    f=open('pattern.txt','a+')
    f.write('INV LEFT ANGLE TRAINGLE NUMBER ROW\n.....................\n')
    for i in range(6,0,-1):
        for j in range(0,i):
         f.write(str(i))
        f.write('\n')
    f.close()
ILATrow()

def ILATcol():
    f=open('pattern.txt','a+')
    f.write('INV LEFT ANGLE TRAINGLE NUMBER COL\n.....................\n')
    for i in range(6,0,-1):
        for j in range(1,i):
         f.write(str(j))
        f.write('\n')
    f.close()
ILATcol()
def ILATcol():
    f=open('pattern.txt','a+')
    f.write('INV LEFT ANGLE TRAINGLE STAR\n.....................\n')
    for i in range(6,0,-1):
        for j in range(1,i):
         f.write('*')
        f.write('\n')
    f.close()
ILATcol()

def ILATup():
    f=open('pattern.txt','a+')
    f.write('INV LEFT ANGLE TRAINGLE NAME UPPER ROW\n.....................\n')
    for i in range(6,0,-1):
        for j in range(1,i):
         f.write(chr(i+63))
        f.write('\n')
    f.close()
ILATup()

def ILATup():
    f=open('pattern.txt','a+')
    f.write('INV LEFT ANGLE TRAINGLE NAME UPPER COL\n.....................\n')
    for i in range(6,0,-1):
        for j in range(1,i):
         f.write(chr(j+64))
        f.write('\n')
    f.close()
ILATup()

def ILATlow():
    f=open('pattern.txt','a+')
    f.write('INV LEFT ANGLE TRAINGLE NAME LOWER ROW\n.....................\n')
    for i in range(6,0,-1):
        for j in range(1,i):
         f.write(chr(i+95))
        f.write('\n')
    f.close()
ILATlow()

def ILATlow():
    f=open('pattern.txt','a+')
    f.write('INV LEFT ANGLE TRAINGLE NAME LOWER COL\n.....................\n')
    for i in range(6,0,-1):
        for j in range(1,i):
         f.write(chr(j+96))
        f.write('\n')
    f.close()
ILATlow()














