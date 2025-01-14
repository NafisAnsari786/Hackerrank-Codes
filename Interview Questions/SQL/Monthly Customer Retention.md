<img src="https://img.shields.io/badge/HARD-darkred" alt="HARD" width="70">
 
![image](https://github.com/user-attachments/assets/5d768851-c7fd-4115-8d05-cc8c2c2a18cd)

**SOLUTION**
```sql
WITH CustomerLag AS (
    SELECT
        CustomerID,
        Month,
        PurchaseCount,
        LAG(PurchaseCount) OVER (PARTITION BY CustomerID ORDER BY FIELD(Month, 'Jan', 'Feb', 'Mar')) AS PreviousPurchaseCount,
        LAG(Month) OVER (PARTITION BY CustomerID ORDER BY FIELD(Month, 'Jan', 'Feb', 'Mar')) AS PreviousMonth
    FROM
        CustomerPurchases
)
SELECT
    CustomerID,
    Month AS CurrentMonth,
    PreviousMonth
FROM
    CustomerLag
WHERE
    PurchaseCount > 0 AND PreviousPurchaseCount > 0;
```

**OUTPUT**

![image](https://github.com/user-attachments/assets/320529d2-0280-4b22-9bc7-beb0f05315fd)
