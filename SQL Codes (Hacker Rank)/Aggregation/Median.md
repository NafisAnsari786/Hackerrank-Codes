<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to 4 decimal places.

Input Format

The STATION table is described as follows:

![image](https://github.com/user-attachments/assets/1e2f4ea4-e0b5-48db-9f04-0a6ee40d7967)

**SOLUTION**

```sql
WITH OrderedValues AS(
    SELECT LAT_N, ROW_NUMBER() OVER (ORDER BY LAT_N) AS row_num,
    COUNT(*) OVER () AS total_rows
    FROM STATION
)
SELECT ROUND(AVG(LAT_N),4) AS MEDIAN
FROM OrderedValues  
WHERE row_num=(total_rows+1)/2
OR (total_rows%2=0 AND row_num IN(total_rows/2, total_rows/2+1));
```
