![image](https://github.com/user-attachments/assets/4b7d7546-4a75-4cb5-b43b-a5c1b69de63b)

**SOLUTION**

```sql
WITH TenureCal AS(
    SELECT 
        Department,
        CASE
            WHEN TerminationDate IS NULL THEN DATEDIFF(CURRENT_DATE, HireDate) / 365.0
            ELSE DATEDIFF(TerminationDate, HireDate) / 365.0
        END AS Tenure
    FROM EmployeeRecords
)
SELECT Department, AVG(Tenure) AS AvgTenure 
FROM TenureCal
GROUP BY Department
```

**OUTPUT**

![image](https://github.com/user-attachments/assets/f8510dd4-aaf5-49a0-b040-709ef2e19615)
