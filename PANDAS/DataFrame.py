import pandas as pd
#DataFrame Using Dictionaries:
print('DataFrame Using Dictionaries:')
print('-'*28)
data={'Name':['priya','kabi','moni','Ragu'],
      'Age':[22,23,21,22],
      'Salary':[50000,60000,67000,55000],
      'Dept':['Gen ai','Testing','Gen ai','Testing']
      }
df=pd.DataFrame(data)
print('employee Data:')
print(df)
print('-'*20)
print('Top Two data only print:')
print(df.head(2))
print('-'*20)
print('Bottom Two Data only print:')
print(df.tail(2))
print('-'*20)
print('Stastical Summary:')
print(df.describe())
print('-'*30)
#Accesing DataFrame:
print('Single Columns:')
print(df.columns)
print(df['Name'])
print(df['Name'][:2])
print('-'*25)
print('Multiple Columns:')
print('Names and Salary:')
print(df[['Name','Salary']])
df.loc[2]
print('Using.loc[] (by label):')
print('\nRow at index 2:')
print(df.loc[2])
print('-'*22)
print('\nspecific cell-Alice"s salary:')
print(df.loc[2,'Salary'])
print('Using.iloc[](by position):')
print('\nfirst 3 rows:')
print(df.iloc[0:3])
print('-'*30)
#Filtering Data:
print(df[df['Dept']=='Gen ai'])
print('-'*30)
print(df[df['Salary']>50000])
print('All Gen ai dept:')
Genai_employees=df[df['Dept']=='Gen ai']
print(Genai_employees)
#Multiple Conditions:(AND)
print('Gen ai employees earning more than 50000:')
filtered=df[(df['Dept']=='Gen ai')&(df['Salary']>50000)]
print(filtered)
#Mulriple Condition:(OR)
print('-'*30)
filter1=df[(df['Dept']=='Gen ai')|(df['Salary']>50000)]
print(filter1)












