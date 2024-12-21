<img src="https://img.shields.io/badge/HARD-darkred" alt="HARD" width="70">

![image](https://github.com/user-attachments/assets/128b97de-9abe-432d-9e2b-08ef633d0d90)

**SOLUTION**
```python
from sklearn.linear_model import LinearRegression

# Create dataset
data = {
    'Hours': [1, 2, 3, 4, 5],
    'Score': [50, 60, 65, 70, 75]
}
df = pd.DataFrame(data)

# Train the model
reg = LinearRegression()
reg.fit(df[['Hours']], df['Score'])

# Make a prediction for 7 hours of study
prediction = reg.predict(pd.DataFrame([[7]], columns=['Hours']))
prediction[0]  # Extract the single value from the prediction array
```
