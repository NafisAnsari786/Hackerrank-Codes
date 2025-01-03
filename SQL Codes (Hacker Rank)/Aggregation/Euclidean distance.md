<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

Consider P1(a,c) and P2(b,d) to be two points on a 2D plane where (a,b) are the respective minimum and maximum values of Northern Latitude (LAT_N) and (c,d) are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

Query the Euclidean Distance between points P1 and P2 and format your answer to display 4 decimal digits. 

Input Format

The STATION table is described as follows: 

![image](https://github.com/user-attachments/assets/755292eb-388a-4907-a199-2e3e4c5b818e)

**SOLUTION**

```sql
SELECT ROUND(
    SQRT(POWER(MAX(LAT_N)-MIN(LAT_N), 2) + POWER(MAX(LONG_W)-MIN(LONG_W),               2)),4)AS EUCLIDEAN_DIST
FROM STATION;
```
