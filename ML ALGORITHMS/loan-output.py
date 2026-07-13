Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

====================== RESTART: C:/Python314/loan_data.py ======================
   person_age person_gender  ... previous_loan_defaults_on_file  loan_status
0        22.0        female  ...                             No            1
1        21.0        female  ...                            Yes            0
2        25.0        female  ...                             No            1
3        23.0        female  ...                             No            1
4        24.0          male  ...                             No            1

[5 rows x 14 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 45000 entries, 0 to 44999
Data columns (total 14 columns):
 #   Column                          Non-Null Count  Dtype  
---  ------                          --------------  -----  
 0   person_age                      45000 non-null  float64
 1   person_gender                   45000 non-null  object 
 2   person_education                45000 non-null  object 
 3   person_income                   45000 non-null  float64
 4   person_emp_exp                  45000 non-null  int64  
 5   person_home_ownership           45000 non-null  object 
 6   loan_amnt                       45000 non-null  float64
 7   loan_intent                     45000 non-null  object 
 8   loan_int_rate                   45000 non-null  float64
 9   loan_percent_income             45000 non-null  float64
 10  cb_person_cred_hist_length      45000 non-null  float64
 11  credit_score                    45000 non-null  int64  
 12  previous_loan_defaults_on_file  45000 non-null  object 
 13  loan_status                     45000 non-null  int64  
dtypes: float64(6), int64(3), object(5)
memory usage: 4.8+ MB
['female' 'male']
['Associate' 'Bachelor' 'Doctorate' 'High School' 'Master']
['MORTGAGE' 'OTHER' 'OWN' 'RENT']
['DEBTCONSOLIDATION' 'EDUCATION' 'HOMEIMPROVEMENT' 'MEDICAL' 'PERSONAL'
 'VENTURE']
['No' 'Yes']

Warning (from warnings module):
  File "C:\Python314\Lib\site-packages\sklearn\linear_model\_logistic.py", line 406
    n_iter_i = _check_optimize_result(
ConvergenceWarning: lbfgs failed to converge after 100 iteration(s) (status=1):
STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT

Increase the number of iterations to improve the convergence (max_iter=100).
You might also want to scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression

Confusion Matrix
[[9939  554]
 [1577 1430]]

Classification Report
              precision    recall  f1-score   support

           0       0.86      0.95      0.90     10493
           1       0.72      0.48      0.57      3007

    accuracy                           0.84     13500
   macro avg       0.79      0.71      0.74     13500
weighted avg       0.83      0.84      0.83     13500


ROC AUC Score
0.8576764765437715
Predicted Loan Approval: [1]
Loan Approved
