<img src="https://img.shields.io/badge/HARD-darkred" alt="HARD" width="70">

![image](https://github.com/user-attachments/assets/15c82ead-de44-4add-bf76-6a9057a63a19)

**SOLUTION**
```sql
WITH ProductSalesRank AS (
    SELECT ProductID, Category, Sales,
    DENSE_RANK() OVER (PARTITION BY Category ORDER BY Sales DESC) AS dense_rank
    FROM ProductSales
)
SELECT ProductID, Category, Sales
FROM ProductSalesRank
WHERE dense_rank <= 3
ORDER BY Category, dense_rank;
```

**OUTPUT**

![image](https://github.com/user-attachments/assets/0899d606-62b3-4a94-a17b-c9820f3b24cb)
