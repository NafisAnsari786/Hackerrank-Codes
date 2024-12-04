<img src="https://img.shields.io/badge/EASY-green" alt="EASY" width="70">

![image](https://github.com/user-attachments/assets/cf585ee5-16b2-471a-b497-186f4a09ae70)

**SOLUTION**

```python
import pandas as pd

# Reading the data from a CSV file
df = pd.read_csv('sales_data.csv')

# Calculating the standard deviation for the 'Sales' column
Sales_std = df['Sales'].std()

# Printing the result
print('Standard Deviation in Sales is:', Sales_std)
```
![image](https://github.com/user-attachments/assets/b825437f-d2a3-4dc5-a054-e3f1e4b24df2)
