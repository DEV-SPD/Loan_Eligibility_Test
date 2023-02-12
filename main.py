import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle



df = pd.read_csv('train.csv')
# print(df.head())

# dropping the missing values
loan_dataset = df.dropna()
# print(loan_dataset.isnull().sum())

loan_dataset = loan_dataset.replace(to_replace='3+', value=4)
# print(loan_dataset['Dependents'].value_counts())

loan_dataset = loan_dataset.replace({"Loan_Status": {'N': 0, 'Y': 1}})
# print(loan_dataset.head())

sns.barplot(x=loan_dataset['Married'], y=loan_dataset['Loan_Status'])
# plt.show()

sns.countplot(x='Education', hue='Loan_Status', data=loan_dataset)
# plt.show()

sns.countplot(x='Gender', hue='Loan_Status', data=loan_dataset)
# plt.show()

# LABEL ENCODING OF CATEGORICAL VALUES
loan_dataset = loan_dataset.replace({"Married": {'Yes': 1, 'No': 0}, "Gender": {'Male': 1, 'Female': 0},
                                     "Self_Employed": {'Yes': 1, 'No': 0},
                                     "Property_Area": {'Rural': 0, 'Urban': 1, 'Semiurban': 2},
                                     "Education": {'Graduate': 1, 'Not Graduate': 0}})


# PREPARING TRAINING DATASET.
x = loan_dataset.drop(columns=['Loan_ID', 'Loan_Status'])
y = loan_dataset['Loan_Status']


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=20)

model = SVC()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

with open('Loan_Eligibility', 'wb') as f:
    pickle.dump(model, f)
