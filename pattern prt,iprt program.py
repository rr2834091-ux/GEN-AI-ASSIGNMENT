def PRT():
    f=open('pattern.txt','a+')
    f.write('NUMBER PRT ROW\n.............\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i))
            f.write(' ')
        f.write('\n')
    f.close()
PRT()

def PRT():
    f=open('pattern.txt','a+')
    f.write('NUMBER PRT COL\n..............\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(j))
            f.write(' ')
        f.write('\n')
    f.close()
PRT()

def PRT():
    f=open('pattern.txt','a+')
    f.write('NUMBER PRT COL\n................\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64))
            f.write(' ')
        f.write('\n')
    f.close()
PRT()

def PRT():
    f=open('pattern.txt','a+')
    f.write('NAME PRT ROW\n.................\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64))
            f.write(' ')
        f.write('\n')
    f.close()
PRT()

def PRT():
    f=open('pattern.txt','a+')
    f.write('LOWER NAME PRT COL\n...............\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(k+65))
            f.write(' ')
        f.write('\n')
    f.close()
PRT()

def PRT():
    f=open('pattern.txt','a+')
    f.write('LOWER NAME PRT ROW\n.................\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+96))
            f.write(' ')
        f.write('\n')
    f.close()
PRT()

def PRT():
    f=open('pattern.txt','a+')
    f.write('LOWER NAME PRT COL\n.................\n')
    for i in range(0,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(k+97))
            f.write(' ')
        f.write('\n')
    f.close()
PRT()

def PRT():
    f=open('pattern.txt','a+')
    f.write('INVERSE UPPER NAME  PRT ROW\n.................\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64))
            f.write(' ')
        f.write('\n')
    f.close()
PRT()

def PRT():
    f=open('pattern.txt','a+')
    f.write('INVERSE UPPER NAME PRT COL\n.................\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(k+65))
            f.write(' ')
        f.write('\n')
    f.close()
PRT()

def PRT():
    f=open('pattern.txt','a+')
    f.write('INVERSE LOWER NAME PRT ROW\n.................\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+96))
            f.write(' ')
        f.write('\n')
    f.close()
PRT()

def PRT():
    f=open('pattern.txt','a+')
    f.write('INVERSE LOWER NAME PRT COL\n.................\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(k+97))
            f.write(' ')
        f.write('\n')
    f.close()
PRT()

def PRT():
    f=open('pattern.txt','a+')
    f.write('INVERSE NUMBER PRT ROW\n.................\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i))
            f.write(' ')
        f.write('\n')
    f.close()
PRT()

def PRT():
    f=open('pattern.txt','a+')
    f.write('INVERSE NUMBER PRT COL\n.................\n')
    for i in range(7,0,-1):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(k))
            f.write(' ')
        f.write('\n')
    f.close()
PRT()
