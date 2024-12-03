![image](https://github.com/user-attachments/assets/f9ed2d30-cf67-4e06-91c9-f99a00c21052)

**SOLUTION**

```sql
WITH HighestAVGSal AS (
    SELECT 
        DEPARTMENT, 
        SALARY,
        RANK() OVER (PARTITION BY DEPARTMENT ORDER BY SALARY DESC) as dense_rank
    FROM EMPLOYEES
)
SELECT 
    DEPARTMENT,
    AVG(SALARY) AS AvgSal
FROM HighestAVGSal
WHERE dense_rank = 1
GROUP BY DEPARTMENT;
```
