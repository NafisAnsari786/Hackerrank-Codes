<img src="https://img.shields.io/badge/HARD-darkred" alt="HARD" width="70">

![image](https://github.com/user-attachments/assets/b9e1b3ca-1a4c-4fc1-94c3-1d960e20547f)

**SOLUTION**
```python
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [200, 220, 250, 300, 310]
})

# Calculate the moving average
df['moving_avg'] = df['Sales'].rolling(window=3).mean()

# Set Month as the index for plotting
df.set_index('Month', inplace=True)

# Plotting the Data 
df[['Sales', 'moving_avg']].plot()
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales with Moving Average')
plt.legend(['Sales', 'Moving Average'])
plt.show()
```

**OUTPUT**

![image](https://github.com/user-attachments/assets/2927efe2-b8e4-4881-b5df-b5dca24a3f2b)


![image](https://github.com/user-attachments/assets/dd77362f-019c-4737-8e94-b716fdb69f77)

