<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

![image](https://github.com/user-attachments/assets/ec826415-5166-4876-8d82-e2e28c9af383)

**OUTPUT**

```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Reading the dataset
df = pd.DataFrame({
    'UserID': [101, 102, 103],
    'Age': [25, 30, 45],
    'Income': [40000, 50000, 60000]
})

# Selecting the columns for scaling
df_scale = df[['Age', 'Income']]

# Initializing the MinMaxScaler
scaler = MinMaxScaler()

# Applying MinMax scaling
scaled_data = scaler.fit_transform(df_scale)

# Converting back to a DataFrame with the original column names
scaled_df = pd.DataFrame(scaled_data, columns=['Age', 'Income'])

# Displaying the scaled data
scaled_df
```
**OUTPUT**
![image](https://github.com/user-attachments/assets/678911cc-0092-4e91-b296-4d492eed9b67)
