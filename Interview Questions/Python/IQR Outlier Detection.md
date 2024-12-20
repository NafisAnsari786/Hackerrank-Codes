<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

![image](https://github.com/user-attachments/assets/c494c84f-880f-4c19-9a0e-5c0a2ed1a561)

**SOLUTION**
```python
import pandas as pd

data = {
    'TransactionID': [1,2,3,4,5],
    'Sales': [100,120,500,110,95]
}

df = pd.DataFrame(data)

# Detecting the Quartiles in Sales
Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)

# Calculating IQR
IQR = Q3 - Q1

# Setting the upper and lower limits
lower_limit = Q1 - 1.5*IQR
upper_limit = Q3 + 1.5*IQR

# Detecting the outliers
outliers = df[(df['Sales'] < lower_limit) | (df['Sales'] > upper_limit)]
outliers
```
**OUTPUT**

![image](https://github.com/user-attachments/assets/ca816168-42bc-4fb7-92ab-c7b1fa41d88f)

