import pandas as pd
print('Vegitables:')
print('-'*20)
Vegitables=['Onion','Tomato','Peans','Carrot','Potato','Cabage','Ladiesfinger','beetroot','Radish','Pumpkin']
Series=pd.Series(Vegitables)
print(Series)
print(type(Vegitables))
#Operations:
#data using Intrinsic Index:
print(Series.loc[5])
print(Series.loc[1])
#Slicing:
print(Series.loc[5:])
print(Series.loc[1:11:2])
#Extrinsic Index:
Series=pd.Series(Vegitables,index=['10kg','15kg','5kg','4kg','8kg','9kg','10kg','20kg','25kg','6kg'])
print('Vegitables weights')
print('-'*34)
print(Vegitables)
#Intrinsic Index:
print(Series['20kg'])
print(Series.loc['25kg'])
print(Series.iloc[4])
#Series Using Dictionary:
print('Vegitable:'' prices:')
Vegitables={'Onion':'160','Tomato':'130','Peans':'90','Carrot':'40','Potato':'120','Cabage':'60','Ladiesfinger':'50','beetroot':'150','Radish':'200','Pumpkin':'100'}
Vegitables=pd.Series(Vegitables)
print(Vegitables)
