import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split #model optimization(to control overfiting and underfiting)
import warnings
warnings.filterwarnings('ignore')

print("Libraries imported successfully!")
# Create sample data:
np.random.seed(42)
house_size = np.array([800, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3500]).reshape(-1, 1)
house_price = np.array([150000, 200000, 250000, 280000, 320000, 350000, 400000, 450000, 500000, 580000])

# Create DataFrame for better visualization
df = pd.DataFrame({'Size (sq ft)': house_size.flatten(), 'Price ($)': house_price})
print("Dataset:")
print(df)
print(f"\nDataset shape: {df.shape}")
X_train,X_test,Y_train,Y_test=train_test_split(house_size,house_price,test_size=0.3,random_state=42)
print(f' Training set size:{len(X_train)}')
print(f' Testing set size:{len(X_test)}')
#using sckit-learn
model=LinearRegression()
model.fit(X_train,Y_train)
#Get Coefficient:
slope=model.coef_[0]
intercept=model.intercept_
print(f'Equation:Price={slope:.2f}xsize+{intercept:.2f}')
print(f'\nSlope:${slope:.2f}per sq ft')
print(f'intercept:${intercept}')
#Make Prediction:
y_pred_train=model.predict(X_train)
y_pred_test=model.predict(X_test)
#make prediction for new house:
new_house_size=np.array([[3100]])
predicted_price=model.predict(new_house_size)[0]
print(f'Predicted Price For 3100 sq ft House:${predicted_price:,.2f}')
