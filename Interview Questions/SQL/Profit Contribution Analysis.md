<img src="https://img.shields.io/badge/HARD-darkred" alt="HARD" width="70">

![image](https://github.com/user-attachments/assets/3982ed5a-083b-43d4-9900-7517365963c8)

**SOLUTION**
```sql
WITH ProfitCal AS (
    SELECT Category,
           SUM(Revenue) - SUM(Cost) AS Profit
    FROM CategoryProfit
    GROUP BY Category
),
TotalProfit AS (
    SELECT SUM(Revenue) - SUM(Cost) AS TotalProfit
    FROM CategoryProfit
)
SELECT p.Category,
       p.Profit,
       ROUND((p.Profit / t.TotalProfit) * 100, 2) AS ContributionPercentage
FROM ProfitCal p
CROSS JOIN TotalProfit t
ORDER BY ContributionPercentage DESC;
```

**OUTPUT**

![image](https://github.com/user-attachments/assets/d09796a6-856a-4e36-a0fc-084f445a56c1)
