heart = [(1,2),(1,3),(1,5),(1,6),
         (2,1),(2,4),(2,7),
         (3,1),(3,7),
         (4,2),(4,6),
         (5,3),(5,5),
         (6,4)]

def hrt():
    for i in range(1, 11):
        for j in range(1, 11):
            if (i, j) in heart:
                print('.', end=' ')
            else:
                print(' ', end=' ')
        print()
hrt()
      
