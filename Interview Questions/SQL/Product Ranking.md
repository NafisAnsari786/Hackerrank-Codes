![image.png](attachment:image.png)

**SOLUTION**

```SQL
WITH TopProducts AS (
    SELECT PRODUCTID, QUANTITYSOLD, REVENUE,
           DENSE_RANK() OVER (ORDER BY REVENUE DESC) AS dense_rnk
    FROM SalesData
)
SELECT PRODUCTID, QUANTITYSOLD, REVENUE 
FROM TopProducts
WHERE dense_rnk <= 3;
```
