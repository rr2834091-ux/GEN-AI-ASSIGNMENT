Circle = [(1,5),(1,6),
         (2,4),(2,7),
         (3,4),(3,7),
         (4,4),(4,7),
         (5,5),(5,6)]

def cic():
    for i in range(1, 10):
        for j in range(1, 10):
            if (i, j) in Circle:
                print('.', end=' ')
            else:
                print(' ', end=' ')
        print()
cic()
      
