<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

![image](https://github.com/user-attachments/assets/2e1a0715-0f12-40ce-9e52-6c54f6585efc)

**SOLUTION**
```sql
WITH DepartmentStats AS (
    SELECT 
        DEPARTMENT, 
        COUNT(*) AS NumEmployees, 
        AVG(OVERTIMEHOURS) AS AvgOvertime
    FROM EMPLOYEEHOURS
    GROUP BY DEPARTMENT
)
SELECT DEPARTMENT, AvgOvertime
FROM DepartmentStats
WHERE NumEmployees > 5;
```
