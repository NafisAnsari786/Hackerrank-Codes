<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

![image](https://github.com/user-attachments/assets/34290515-7c8b-462b-b2b8-cd62719e85c3)

**SOLUTION**

```python
import pandas as pd 
df=pd.read_csv('sales_data.csv')

unique_df = df.drop_duplicates(keep='first')

#Optional, to check how many duplicates were removed
print(f"Number of duplicates removed: {len(df) - len(unique_df)}")

unique_df
```
**OUTPUT**

![image](https://github.com/user-attachments/assets/0e3d9db1-5663-4529-abd5-eb4240eb72fa)
