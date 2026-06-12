Circle = [(1,5),(1,6),(2,4),(2,7),(3,4),(3,7),(4,4),(4,7),(5,5),(5,6)]
def cic():
    print('circle:')
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in Circle:
                print('.', end=' ')
            else:
                print(' ', end=' ')
        print()
cic()
print('-'*15)

ovall=[(2,3),(2,4),(2,5),(3,2),(3,6),(4,2),(4,6),(5,3),(5,4),(5,5)]
def ova():
    print('ovall:')
    for i in range(1,10):
        for j in range(1,10):
            if(i,j) in ovall:
                print('.',end=' ')
            else:
                print(' ',end=' ')
        print()
ova()
print('-'*15)
square=[(2,3),(2,4),(2,5),(2,6),(2,7),(3,3),(3,7),(4,3),(4,7),(5,3),(5,7),(6,3),(6,4),(6,5),(6,6),(6,7)]
def sq2():
    print('Square:')
    for i in range(1,10):
        for j in range(1,10):
            if(i,j) in square:
                print('.',end=' ')
            else:
                print(' ',end=' ')
        print()
sq2()
print('-'*15)

Rhombus=[(3,3),(3,4),(3,5),(3,6),(3,7),(5,2),(5,6),(7,1),(7,2),(7,3),(7,4),(7,5)]
def rho():
    print('Rhombus:')
    for i in range(1,10):
        for j in range(1,10):
            if(i,j) in Rhombus:
                print('.',end=' ')
            else:
                print(' ',end=' ')
        print()
rho()
print('-'*15)





      
