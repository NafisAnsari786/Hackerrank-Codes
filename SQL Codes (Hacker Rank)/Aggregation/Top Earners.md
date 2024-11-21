<img src="https://img.shields.io/badge/EASY-green" alt="EASY" width="70">

We define an employee's total earnings to be their monthly salary * months worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table.
Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. 
Then print these values as 2 space-separated integers.

Input Format

The Employee table containing employee data for a company is described as follows:

![image](https://github.com/user-attachments/assets/2a1ddebc-dd05-492e-9154-cf8a48c459e8)

where employee_id is an employee's ID number, name is their name, months is the total number of months they've been working for the company, and salary is the their monthly salary.

Sample Input
![image](https://github.com/user-attachments/assets/e611db47-6e70-4df6-97cf-124b5e9dc617)

Sample Output

69952 1

**SOLUTION**

```sql
SELECT (SALARY*MONTHS) AS TOTAL_EARNS,
COUNT(*) FROM EMPLOYEE AS MAX_EARN_EMPL
GROUP BY TOTAL_EARNS
ORDER BY TOTAL_EARNS DESC LIMIT 1;
```

