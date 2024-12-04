![image](https://github.com/user-attachments/assets/1435a674-a3dd-4eeb-8248-2f76e1d3b019)


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
