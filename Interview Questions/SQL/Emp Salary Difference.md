<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

![image](https://github.com/user-attachments/assets/af9ea6ed-5f43-4dbf-adc0-dd46e50a1b19)

**SOLUTION**

```sql
WITH SalaryCal AS (
    SELECT Department, MAX(Salary) AS Max_sal, MIN(Salary) AS Min_Sal
    FROM EmployeeSalaries
    GROUP BY Department
)
SELECT Department, (Max_sal - Min_Sal) AS SalaryDifference
FROM SalaryCal;
```

**OUTPUT**

![image](https://github.com/user-attachments/assets/07ba7882-b9af-4ac8-824a-f6d7ec26008d)
