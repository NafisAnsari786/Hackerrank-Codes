SQL Query Question with Table Schemas   
Question:
Given the following table schemas, write a SQL query to display the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees for each company. The output should be ordered by the company_code in ascending order. Please note that:

The tables may contain duplicate records.
The company_code is a string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending order should be C_1, C_10, and C_2.
Table Schemas:
Company: This table contains information about each company.
 
company_code: The code of the company (string).
founder: The founder of the company (string).
Lead_Manager: This table contains information about lead managers.

lead_manager_code: The code of the lead manager (string).
company_code: The code of the company the lead manager works for (string).
Senior_Manager: This table contains information about senior managers.
 
senior_manager_code: The code of the senior manager (string).
lead_manager_code: The code of the lead manager supervising the senior manager (string).
company_code: The code of the company the senior manager works for (string).
Manager: This table contains information about managers.

manager_code: The code of the manager (string).
senior_manager_code: The code of the senior manager supervising the manager (string).
lead_manager_code: The code of the lead manager supervising the manager (string).
company_code: The code of the company the manager works for (string).
Employee: This table contains information about employees.

employee_code: The code of the employee (string).
manager_code: The code of the manager supervising the employee (string).
senior_manager_code: The code of the senior manager supervising the employee (string).
lead_manager_code: The code of the lead manager supervising the employee (string).
company_code: The code of the company the employee works for (string).

**SOLUTION**
```sql
SELECT 
    c.company_code, 
    c.founder,  
    COUNT(DISTINCT lm.lead_manager_code) AS total_lead_managers,
    COUNT(DISTINCT sm.senior_manager_code) AS total_senior_managers,
    COUNT(DISTINCT m.manager_code) AS total_managers,
    COUNT(DISTINCT e.employee_code) AS total_employees 
FROM 
    Company c
LEFT JOIN   
    Lead_Manager lm ON c.company_code = lm.company_code
LEFT JOIN 
    Senior_Manager sm ON c.company_code = sm.company_code
LEFT JOIN 
    Manager m ON c.company_code = m.company_code
LEFT JOIN 
    Employee e ON c.company_code = e.company_code
GROUP BY 
    c.company_code, c.founder
ORDER BY 
    c.company_code ASC;
```
