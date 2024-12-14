<img src="https://img.shields.io/badge/HARD-darkred" alt="HARD" width="70">

![image](https://github.com/user-attachments/assets/773aeb8a-79ae-45b1-bcfd-b59fef2a8700)

**SOLUTION**
```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv('customer_data.csv')

# Check for missing values (your code already includes this)
df.isnull().sum()

# Feature scaling
scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(df[['Age', 'AnnualIncome']])

# Prepare independent and dependent variables
X = pd.DataFrame(scaled_features, columns=['Age', 'AnnualIncome'])
y = df['MadePurchase']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

# Logistic Regression Model
log_clf = LogisticRegression()
log_clf.fit(X_train, y_train)

# Model performance
accuracy = log_clf.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# To predict for new data
# Scale new data before prediction
new_data = scaler.transform([[36, 78000]])
prediction = log_clf.predict(new_data)
print("Prediction for new customer:", prediction)
```

**OUTPUT**
![image](https://github.com/user-attachments/assets/e15fb874-a2c4-4dd1-849d-e02142985b47)
