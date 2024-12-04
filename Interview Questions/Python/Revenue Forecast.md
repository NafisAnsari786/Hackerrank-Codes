<img src="https://img.shields.io/badge/EASY-green" alt="EASY" width="70">

![image](https://github.com/user-attachments/assets/701b89cc-ef04-46f8-b441-89699fcedee4)

**SOLUTION**

```python
import pandas as pd
 
# Load the sales data
df = pd.read_csv('monthly_sales.csv')

# Calculate average monthly revenue
avg_monthly_rev = df['Revenue'].mean()

# Forecast for the next 6 months
forecast_period = 6
forecast = [avg_monthly_rev] * forecast_period

# Creating a DataFrame for forecasted values
forecast_df = pd.DataFrame({'Month': range(1, forecast_period + 1), 'Forecast': forecast})

# Displaying the forecasted data
print(forecast_df)
```

![image](https://github.com/user-attachments/assets/3eb650b0-09be-415d-b8ef-f46764f790c6)
