![image](https://github.com/user-attachments/assets/5a6d86bd-a7fc-4c8b-a581-6c5517d8c700)

**SOLUTION**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('stock_prices.csv')

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Calculate the 3-day moving average
df['moving_avg'] = df['StockPrice'].rolling(window=3).mean()

# Plotting the data
df[['StockPrice', 'moving_avg']].plot(x='Date', label='Stocks')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Stock Price with Moving Average')
plt.show()

```
**OUTPUT**

![image](https://github.com/user-attachments/assets/f390b688-35b3-49e5-920f-ab5059a51d63)

