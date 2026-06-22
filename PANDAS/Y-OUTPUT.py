Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
====================== RESTART: C:/Python314/DataFrame.py ======================
DataFrame Using Dictionaries:
----------------------------
employee Data:
    Name  Age  Salary     Dept
0  priya   22   50000   Gen ai
1   kabi   23   60000  Testing
2   moni   21   67000   Gen ai
3   Ragu   22   55000  Testing
--------------------
Top Two data only print:
    Name  Age  Salary     Dept
0  priya   22   50000   Gen ai
1   kabi   23   60000  Testing
--------------------
Bottom Two Data only print:
   Name  Age  Salary     Dept
2  moni   21   67000   Gen ai
3  Ragu   22   55000  Testing
--------------------
Stastical Summary:
             Age        Salary
count   4.000000      4.000000
mean   22.000000  58000.000000
std     0.816497   7257.180352
min    21.000000  50000.000000
25%    21.750000  53750.000000
50%    22.000000  57500.000000
75%    22.250000  61750.000000
max    23.000000  67000.000000
------------------------------
Single Columns:
Index(['Name', 'Age', 'Salary', 'Dept'], dtype='object')
0    priya
1     kabi
2     moni
3     Ragu
Name: Name, dtype: object
0    priya
1     kabi
Name: Name, dtype: object
-------------------------
Multiple Columns:
Names and Salary:
    Name  Salary
0  priya   50000
1   kabi   60000
2   moni   67000
3   Ragu   55000
Using.loc[] (by label):

Row at index 2:
Name        moni
Age           21
Salary     67000
Dept      Gen ai
Name: 2, dtype: object
----------------------

specific cell-Alice"s salary:
67000
Using.iloc[](by position):

first 3 rows:
    Name  Age  Salary     Dept
0  priya   22   50000   Gen ai
1   kabi   23   60000  Testing
2   moni   21   67000   Gen ai
------------------------------
    Name  Age  Salary    Dept
0  priya   22   50000  Gen ai
2   moni   21   67000  Gen ai
------------------------------
   Name  Age  Salary     Dept
1  kabi   23   60000  Testing
2  moni   21   67000   Gen ai
3  Ragu   22   55000  Testing
All Gen ai dept:
    Name  Age  Salary    Dept
0  priya   22   50000  Gen ai
2   moni   21   67000  Gen ai
Gen ai employees earning more than 50000:
   Name  Age  Salary    Dept
2  moni   21   67000  Gen ai
------------------------------
    Name  Age  Salary     Dept
0  priya   22   50000   Gen ai
1   kabi   23   60000  Testing
2   moni   21   67000   Gen ai
3   Ragu   22   55000  Testing
