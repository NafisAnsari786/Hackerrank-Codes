<img src="https://img.shields.io/badge/HARD-darkred" alt="HARD" width="70">

![image](https://github.com/user-attachments/assets/3982ed5a-083b-43d4-9900-7517365963c8)

**SOLUTION**
```sql
WITH CategoryProfitSummary AS (
    SELECT
        Category,
        Revenue,
        Cost,
        Revenue - Cost AS Profit,
        SUM(Revenue - Cost) OVER () AS TotalProfit
    FROM
        CategoryProfit
)
SELECT
    Category,
    Profit,
    ROUND((Profit / TotalProfit) * 100, 2) AS ProfitContributionPercentage
FROM
    CategoryProfitSummary
ORDER BY
    ProfitContributionPercentage DESC;
```

**OUTPUT**

![image](https://github.com/user-attachments/assets/d09796a6-856a-4e36-a0fc-084f445a56c1)
