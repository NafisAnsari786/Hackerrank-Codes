<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

![image](https://github.com/user-attachments/assets/2541a081-6b59-45bb-abd3-a3e869309305)

**SOLUTION**
```python
import pandas as pd

# Sample dataset based on the given table
data = {
    'ProductID': [201, 202, 203, 204, 205],
    'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Clothing'],
    'Sales': [10, 15, 5, 10, 20],
    'Price': [500, 600, 300, 400, 50]
}

# Create DataFrame
df = pd.DataFrame(data)

# Group by 'Category' and calculate total sales and average price
aggregated_data = df.groupby('Category').agg(
    total_sales=('Sales', 'sum'),
    average_price=('Price', 'mean')
)

aggregated_data
```
**OUTPUT**

![image](https://github.com/user-attachments/assets/763c9659-c2f4-4c47-9d1b-1c9cc345aa22)
