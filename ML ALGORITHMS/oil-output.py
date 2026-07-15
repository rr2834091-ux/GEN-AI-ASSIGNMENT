Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
====================== RESTART: C:/Python314/Oil Sales.py ======================
Libraries imported successfully!
       city  ... average_price
0   AL BAHA  ...          27.6
1  AL KHARJ  ...          41.0
2    RIYADH  ...         101.0
3    DAMMAM  ...          61.0
4     JAZAN  ...          81.0

[5 rows x 13 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2000 entries, 0 to 1999
Data columns (total 13 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   city           2000 non-null   object 
 1   store_name     2000 non-null   object 
 2   manufacturer   2000 non-null   object 
 3   brand          2000 non-null   object 
 4   class          2000 non-null   object 
 5   size           2000 non-null   object 
 6   sku            2000 non-null   object 
 7   price_bracket  2000 non-null   object 
 8   year           2000 non-null   int64  
 9   month          2000 non-null   int64  
 10  value_sales    2000 non-null   float64
 11  volume_sales   2000 non-null   float64
 12  average_price  2000 non-null   float64
dtypes: float64(3), int64(2), object(8)
memory usage: 203.3+ KB
None
city             0
store_name       0
manufacturer     0
brand            0
class            0
size             0
sku              0
price_bracket    0
year             0
month            0
value_sales      0
volume_sales     0
average_price    0
dtype: int64

Model Performance
Mean Squared Error(MSE): 23.283147074008223
Root mean squared Error(RMSE): 4.825261347741511
R2 Score: 0.9695359853307112
      Actual Price  Predicted Price
1860         101.0       106.192020
353           40.0        46.064377
1333          90.0        94.716323
905           30.0        26.372873
1289          81.0        82.745088
1273          60.0        60.589671
938           91.0        86.976465
1731          30.0        27.767530
65            81.0        82.811831
1323          60.0        55.795541
