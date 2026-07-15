import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

print("Libraries imported successfully!")
#Read the Datasets:
df=pd.read_csv(r'C:\Users\RAGUL R\Downloads\archive (3).zip')
#display first 5 rows:
print(df.head())
print(df.info())
#removing the missing values:
df.dropna()
#Check the Missing values:
print(df.isnull().sum())
#categorical col to numerical values:
df = pd.get_dummies(df, drop_first=True)
#Features(X) and Target(Y):
X=df.drop('average_price',axis=1)
Y=df['average_price']
#Split the data:
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)
#Model()
model=LinearRegression()
model.fit(X_train,Y_train)
#predict data:
Y_pred=model.predict(X_test)
#Evalution:
print('\nModel Performance')
print('Mean Squared Error(MSE):',mean_squared_error(Y_test,Y_pred))
print('Root mean squared Error(RMSE):',np.sqrt(mean_squared_error(Y_test,Y_pred)))
print('R2 Score:',r2_score(Y_test,Y_pred))
#predicted vs actual price:
result=pd.DataFrame({'Actual Price':Y_test,
                     'Predicted Price':Y_pred})
print(result.head(10))
