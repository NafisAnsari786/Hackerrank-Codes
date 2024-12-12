<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

![image](https://github.com/user-attachments/assets/cdc1b35f-ec1b-4c8c-8596-0cbd1486ac33)

**SOLUTION**
```sql
WITH MonthlyGrowth AS ( 
    SELECT 
        Month, 
        Year,
        SUM(TotalSales) AS SalesPerMonth, 
        SUM(SUM(TotalSales)) OVER (PARTITION BY Year) AS AnnualSales
    FROM MonthlySales
    GROUP BY Month, Year
)
SELECT 
    Year, 
    Month, 
    SalesPerMonth, 
    AnnualSales,
    ROUND((SalesPerMonth / AnnualSales) * 100, 2) AS SalesGrowthPercent
FROM MonthlyGrowth
ORDER BY Year, Month; 

```

**OUTPUT**
![image](https://github.com/user-attachments/assets/f28c1d2f-9991-4ec1-b878-51f616d5e9ae)
