<img src="https://img.shields.io/badge/HARD-darkred" alt="HARD" width="70">

![image](https://github.com/user-attachments/assets/c96630a1-0f9c-4f3f-97b9-32c1b024f39c)

**SOLUTION**
```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

data = {
    'Feature1': [1.5, 3.0, 2.5, 1.0],
    'Feature2': [2.0, 4.0, 3.5, 1.5],
    'Label': [0, 1, 0, 1]
}

df = pd.DataFrame(data)

#Normalize using Min Max Scaler
scaler = MinMaxScaler()
scaled_df = scaler.fit_transform(df[['Feature1', 'Feature2']])

X = pd.DataFrame(scaled_df, columns = ['Feature1', 'Feature2'])
y = df['Label']

#Split the dataset to trian and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

X_train
```

**Output**

![image](https://github.com/user-attachments/assets/c94f21bf-e125-44e9-8e76-d5c4c76a40a7)
