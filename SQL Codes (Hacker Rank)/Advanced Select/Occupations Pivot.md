Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

Note: Print NULL when there are no more names corresponding to an occupation.

Input Format

The OCCUPATIONS table is described as follows:

![image](https://github.com/user-attachments/assets/9d428ccf-3b26-4b31-b6a0-46e3b23bb04b)

Occupation will only contain one of the following values: Doctor, Professor, Singer or Actor.

Sample Input

![image](https://github.com/user-attachments/assets/5f2439bf-a1bf-485e-8e35-b07f4a31bd6f)

Sample Output

Jenny    Ashley     Meera  Jane
Samantha Christeen  Priya  Julia
NULL     Ketty      NULL   Maria

**Solution**

```sql
SOLUTION 1:

WITH RankedOccupations AS(
    SELECT NAME, OCCUPATION, DENSE_RANK() OVER (PARTITION BY OCCUPATION ORDER BY NAME) AS dense_rank
    FROM OCCUPATIONS
)
SELECT  [DOCTOR],[PROFESSOR],[SINGER],[ACTOR]  FROM RankedOccupations
PIVOT(
    MAX(NAME)
    FOR OCCUPATION IN ([DOCTOR],[PROFESSOR],[SINGER],[ACTOR])
) AS PivotedTable
ORDER BY dense_rank;

SOLUTION 2:

WITH RankedOccupations AS(
    SELECT NAME, OCCUPATION, DENSE_RANK() OVER (PARTITION BY OCCUPATION ORDER BY NAME) AS dense_rank
    FROM OCCUPATIONS
)
SELECT
    MAX(CASE WHEN OCCUPATION='DOCTOR' THEN NAME ELSE NULL END) AS DOCTOR,
    MAX(CASE WHEN OCCUPATION='PROFESSOR' THEN NAME ELSE NULL END) AS PROFESSOR,
    MAX(CASE WHEN OCCUPATION='SINGER' THEN NAME ELSE NULL END) AS SINGER,
    MAX(CASE WHEN OCCUPATION='ACTOR' THEN NAME ELSE NULL END) AS ACTOR
FROM RankedOccupations
GROUP BY dense_rank
ORDER BY dense_rank;
```
