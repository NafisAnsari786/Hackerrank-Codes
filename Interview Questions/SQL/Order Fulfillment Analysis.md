<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

![image](https://github.com/user-attachments/assets/6ef46c24-ad2e-4390-80ba-f57db199d1c7)

**SOLUTION**
```sql
WITH FulfilledOrders AS (
    SELECT CustomerID, COUNT(*) AS FulfilledOrders
    FROM Orders
    WHERE OrderStatus = 'Fulfilled'
    GROUP BY CustomerID
),
TotalOrders AS (
    SELECT CustomerID, COUNT(*) AS TotalOrders
    FROM Orders
    GROUP BY CustomerID
)
SELECT
    FulfilledOrders.CustomerID,
    (FulfilledOrders.FulfilledOrders / TotalOrders.TotalOrders) * 100 AS FulfillmentPercentage
FROM
    FulfilledOrders
JOIN
    TotalOrders ON FulfilledOrders.CustomerID = TotalOrders.CustomerID;
```

**OUTPUT**

![image](https://github.com/user-attachments/assets/7468dc30-a4a1-4b5c-8913-6aefaf536045)
