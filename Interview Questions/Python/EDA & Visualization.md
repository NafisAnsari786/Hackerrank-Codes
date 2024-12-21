<img src="https://img.shields.io/badge/HARD-darkred" alt="HARD" width="70">

![image](https://github.com/user-attachments/assets/09876310-6ecf-40aa-a791-5f2eda5b8bba)

**SOLUTION**
```python
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Category': ['Electronics', 'Furniture', 'Clothing'],
    'Revenue': [50000, 30000, 20000]
}

df = pd.DataFrame(data)

# Performing EDA
df.isnull().sum()

df.describe()

df.info()

# Revenue distribution per category
revenue_per_cat = df.groupby('Category')['Revenue'].agg('sum')

#Visualize the bar chart
revenue_per_cat.plot(kind='bar', color='limegreen', title='Revenue Per Category')
plt.xlabel('Products Category')
plt.ylabel('Revenue')
plt.xticks(rotation=45)

# Add revenue values above the bars (OPTIONAL)
for index, value in enumerate(revenue_per_cat):
    plt.text(index, value, str(value), ha='center', va='bottom')

plt.tight_layout()
plt.show()
```
**OUTPUT**

![image](https://github.com/user-attachments/assets/4d15d5a4-655d-4294-89bf-299b438f9db2)
