<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

![image](https://github.com/user-attachments/assets/69e2a1e4-998f-4fdb-9aed-5a2b91739994)

**SOLUTION**
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data
df=pd.read_csv('sales.csv')

# Group by 'Category' and calculate total revenue for each category
total_revenue=df.groupby('Category')['Revenue'].sum()

# Find the top-performing category
top_cattegory=total_revenue.idxmax()
top_revenue=total_revenue.max()

print("Top performing Category: {top_cattegory} with Revenue: {top_revenue}")

# Plot the total revenue for each category
plt.figure(figsize=(10,8))
total_revenue.plot(kind='bar', color='salmon')
plt.xlabel('Category')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()
```
