<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

![image](https://github.com/user-attachments/assets/f9870f19-9422-4465-93ba-421c5bd65be3)

**SOLUTION**

```python
# Confusion Matrix Values
TP = 50
FP = 5
TN = 35
FN = 10

#Precision 
precision = TP / (TP + FP)

#Recall
recall = TP / (TP + FP)

# F1 Score 
f1_score = 2 * (precision * recall) / (precision + recall)

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1_score:.4f}")
```

**OUTPUT**

![Uploading image.png…]()
