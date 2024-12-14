<img src="https://img.shields.io/badge/EASY-green" alt="EASY" width="70">

![image](https://github.com/user-attachments/assets/3e9c1c16-bb98-4696-b183-2b550eb7c471)

**SOLUTION**
```python
import pandas as pd

df = pd.read_csv('product_data.csv')

# Checking for missing values
df.isnull().sum()

# Identifying numerical and categorical columns
num_cols = ['ProductID', 'Price']
cat_cols = ['ProductName', 'Category']

# Handling missing values for numerical columns using mean
df[num_cols] = df[num_cols].fillna(df[num_cols].mean(), axis=0)

# Handling missing values for categorical columns using mode (with iloc[0])
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0], axis=0)

df.head()
```

**OUTPUT**
![image](https://github.com/user-attachments/assets/6c6e42ef-c5b1-471f-9925-af55e4ccccc7)
