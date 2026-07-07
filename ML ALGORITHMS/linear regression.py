import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')
print("Libraries imported successfully!")
print('Ice Cream Details:')
np.random.seed(42)
icenames=np.array(['Bacon','Beer','Biscuit Tortoni','Black raspberry','Blue moon','Brown bread','Butter Brickle','Butter pecan'])
icecount=np.array([10,20,25,30,40,50,60,70]).reshape(-1,1)
icesales=np.array([100,200,400,500,200,250,300,200])
iceprice=np.array(['300Rs','400Rs','500Rs','600Rs','700Rs','800Rs','900Rs','150Rs'])
df=pd.DataFrame({'IceCream(Names)':icenames,'Count(Ice cream)':icecount.flatten(),'Sales(Ice)':icesales, 'Prices':iceprice})
print('Menu card:')
print(df)
