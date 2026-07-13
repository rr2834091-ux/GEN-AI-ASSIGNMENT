import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve
# Read the dataset:
df=pd.read_csv(r"C:\Users\RAGUL R\Downloads\archive.zip")
#Display the first 5 Rows:
print(df.head())
#information of the data:
df.info()
#Remove the missing values:
df.dropna()
#LabelEncoder:
le=LabelEncoder()
df['person_gender']=le.fit_transform(df['person_gender'])
print(le.classes_)
df['person_education']=le.fit_transform(df['person_education'])
print(le.classes_)
df['person_home_ownership']=le.fit_transform(df['person_home_ownership'])
print(le.classes_)
df['loan_intent']=le.fit_transform(df['loan_intent'])
print(le.classes_)
df['previous_loan_defaults_on_file']=le.fit_transform(df['previous_loan_defaults_on_file'])
print(le.classes_)
#Features(x) and Target(y):
X=df.drop('loan_status',axis=1)
Y=df['loan_status']
#split the data:
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)
#train the model:
model=LogisticRegression()
model.fit(X_train,Y_train)
#predict:
Y_pred=model.predict(X_test)
#Evalution:
print("\nConfusion Matrix")
print(confusion_matrix(Y_test, Y_pred))

print("\nClassification Report")
print(classification_report(Y_test, Y_pred))

print("\nROC AUC Score")
print(roc_auc_score(Y_test, model.predict_proba(X_test)[:,1]))

#new loan data:
new_customer=pd.DataFrame({
    'person_age':[26],
    'person_gender':[1],
    'person_education':[1],
    'person_income':[200000],
    'person_emp_exp':[10],
    'person_home_ownership':[2],
    'loan_amnt':[40000],
    'loan_intent':[1],
    'loan_int_rate':[20],
    'loan_percent_income':[50],
    'cb_person_cred_hist_length':[4],
    'credit_score':[800],
    'previous_loan_defaults_on_file':[0]
})
#predicted loan status:
new_customer=new_customer[X.columns]
predicted_loan=model.predict(new_customer)
print('Predicted Loan Approval:',predicted_loan)
if predicted_loan[0]== 1:
    print("Loan Approved")
else:
    print("Loan Not Approved")
