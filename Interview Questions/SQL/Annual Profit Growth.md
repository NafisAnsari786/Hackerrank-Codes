<img src="https://img.shields.io/badge/HARD-darkred" alt="HARD" width="70">

![image](https://github.com/user-attachments/assets/8e96c929-acc2-40da-8d83-c5a3a3f3330e)

**SOLUTION**
```sql
WITH AnnualProfit AS (
    SELECT Year,
    (SUM(Revenue) - SUM(Expenses)) AS Profit
    FROM AnnualProfits
    GROUP BY Year
),
ProfitGrowth AS(
    SELECT a1.Year AS Current_Year,
    a2.Year As Next_Year,
    a1.Profit AS Current_Profit,
    a2.Profit AS Next_Profit,
    ROUND(((a2.Profit - a1.Profit)/a1.Profit)*100, 2) AS Growth_Percentage
    FROM AnnualProfit a1
    INNER JOIN AnnualProfit a2
    ON a2.Year = a1.Year + 1
)
SELECT Current_Year,
Next_Year,
Current_Profit,
Next_Profit,
Growth_Percentage
FROM ProfitGrowth
ORDER BY Current_Year;
```

**OUTPUT**
![image](https://github.com/user-attachments/assets/ed6f6e8d-7114-4fef-9832-fb95a10a0971)
