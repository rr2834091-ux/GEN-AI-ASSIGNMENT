#Series
import pandas as pd
Games=pd.Series(['Cricket','Kabadi','Volyball','Football'])
print('Series of Games')
print(Games)
Scores=pd.Series([40,103,65,39,71,43,10],index=['KL Rahul','Dhoni','Virat','Hardik','Ishan','Ruthuraj','Ashwin'])
print("Players scores:")
print(Scores)
Scores=pd.Series([40,103,65,39,71,43,10],index=['KL Rahul','Dhoni','Virat','Hardik','Ishan','Ruthuraj','Ashwin'])
print('Captian Cool:')
print('voice captain:')
print(Scores)
print('only Dhoni  Scores:',Scores['Dhoni'])
print('only Virat  Scores:',Scores['Virat'])
#series from a dictionary:
Scores=pd.Series({'KL Rahul':40,'Dhoni':103,'Virat':65,'Hardik':39,'Ishan':71,'Ruthuraj':43,'Ashwin':10})
print('Player Scores:')
print(Scores)
#dataframe:
IND_Team={'name':['KL RAHUL','Dhoni','Virat','Hardik'],
      'scores':[40,103,65,39]}
df=pd.DataFrame(IND_Team)
print('IND Team Scores:247')
print(df)


