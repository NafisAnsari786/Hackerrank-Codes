<img  src="https://img.shields.io/badge/HARD-darkred" alt="HARD" width="70">

![image](https://github.com/user-attachments/assets/0b3c68cf-95d1-4eb1-90dc-545d80a30b41)

**SOLUTION**

```sql
WITH CustStats AS (
    SELECT CustomerID, Month, PurchaseCount,
    LAG(PurchaseCount, 1) OVER (PARTITION BY CustomerID ORDER BY Month) AS PreviousPurchase,
    LAG(PurchaseCount, 2) OVER (PARTITION BY CustomerID ORDER BY Month) AS PurchaseTwoMonthsAgo
    FROM CustomerPurchases
),
CustomerChurn AS (
    SELECT CustomerID
    FROM CustStats
    WHERE PurchaseCount = 0
    AND PreviousPurchase = 0
    AND PurchaseTwoMonthsAgo > 0
)
SELECT DISTINCT CustomerID
FROM CustomerChurn;
```
**OUTPUT**

![image](https://github.com/user-attachments/assets/75a03816-7d6a-4489-929c-d13a144ec890)
