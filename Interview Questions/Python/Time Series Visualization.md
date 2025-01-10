<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

![image](https://github.com/user-attachments/assets/a24282fd-8c38-4b23-8d22-941c78c66105)

**SOLUTION**
 
```python
import pandas as pd
import matplotlib.pyplot as plt 

# Load the dataset
df = pd.read_csv('sales_trends.csv')

# Ensure the 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort the data by Date (optional but good practice for time series visualization)
df = df.sort_values(by='Date')

# Plot the time series
plt.plot(df['Date'], df['Sales'], color='skyblue')  # Explicitly set Date as x-axis and Sales as y-axis
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Trends Over Time')  # Add a title for better visualization
plt.grid(True)  # Optional: Adds a grid for easier trend analysis
plt.show()
```
