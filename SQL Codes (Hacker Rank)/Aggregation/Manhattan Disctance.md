<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

Consider P1(a,b) and P2(c,d) to be two points on a 2D plane.

- a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
- b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
- c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
- d happens to equal the maximum value in Western Longitude (LONG_W in STATION).
- 
Query the Manhattan Distance between points P1 and P2 and round it to a scale of 4 decimal places.

Input Format

The STATION table is described as follows:

![image](https://github.com/user-attachments/assets/c11860e4-3f80-42dc-878c-bf43b480be10)

where LAT_N is the northern latitude and LONG_W is the western longitude.

**SOLUTION**

```sql
SELECT ROUND(ABS(MIN(LAT_N)-MAX(LAT_N))+ABS(MIN(LONG_W)-MAX(LONG_W)),4) AS MANHAT_DIST
FROM STATION;
```
