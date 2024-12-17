<img src="https://img.shields.io/badge/HARD-darkred" alt="HARD" width="70">

![image](https://github.com/user-attachments/assets/4ea40dcf-910e-468c-828c-af9e5a613124)

**SOLUTION**

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Dataset
df = pd.DataFrame({
    'CustomerID': [101, 102, 103, 104, 105],
    'Age': [25, 40, 35, 30, 45],
    'Income': [30000, 80000, 50000, 40000, 70000],
    'HighSpender': [0, 1, 0, 1, 1]
})

# Splitting features (X) and target (y)
X = df[['Age', 'Income']]
y = df['HighSpender']

# Scaling the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size = 0.2, random_state = 20)

# KNN Classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Evaluating the model
accuracy = knn.score(X_test, y_test)
print("Model Accuracy:", accuracy)

#To predict if the person is a HighSpender
new_data = pd.DataFrame([[36, 85000]], columns=['Age', 'Income'])
new_data_scaled = scaler.transform(new_data)
prediction = knn.predict(new_data_scaled)
print("Prediction for new data:", prediction)
```

**OUTPUT**

![image](https://github.com/user-attachments/assets/96cef52e-d489-4d64-9f2d-37d35eddfbef)

