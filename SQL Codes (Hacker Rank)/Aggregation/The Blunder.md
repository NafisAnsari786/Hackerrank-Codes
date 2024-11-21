# ![EASY](https://img.shields.io/badge/EASY-green)

✅ **EASY**



### **Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's  key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.**
Write a query calculating the amount of error (i.e.: actual - miscalculated average monthly salaries), and round it up to the next integer.

Input Format

The EMPLOYEES table is described as follows:

![image](https://github.com/user-attachments/assets/f38b9371-0f44-4735-87c0-dda7fa7230c8)

Note: Salary is per month.

Sample Input
![image](https://github.com/user-attachments/assets/1f2becea-411a-449a-a83e-e22f454595bd)

Sample Output

2061

**SOLUTION**

```sql
SELECT CEIL(AVG(SALARY)-AVG(REPLACE(SALARY,'0',''))) AS ERROR_AMT
FROM EMPLOYEES;

-- CEIL IS USED TO ALWAYS ROUND THE NUMBER TO THE NEXT INTEGER (3.14 -> 4, -2.78 -> -2) IF NO DECIMAL THEN RETURNS THE SAME INTEGER( CEIL(5) = 5)

-- ROUND IS USED TO ROUND THE NUMBER TO THE NEAREST INTEGER BASED ON (If the decimal part is 0.5 or greater, it rounds up [ROUND(3.5) = 4 ]) & (If the decimal part is less than 0.5, it rounds down [ROUND(3.14) = 3])

-- FLOOR IS USED TO ALWAYS ROUND number down to the nearest integer. (FLOOR(3.14) = 3),(FLOOR(-2.718) = -3). IF NO DECIMAL THEN RETURNS THE SAME INTEGER (FLOOR(5) = 5)
```
