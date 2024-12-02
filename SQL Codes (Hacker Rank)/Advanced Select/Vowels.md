<img src="https://img.shields.io/badge/EASY-green" alt="EASY" width="70">


### **Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.**

Input Format

The STATION table is described as follows:

https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg

**SOLUTION** 

```SQL
SELECT DISTINCT(CITY) FROM STATION
WHERE CITY NOT REGEXP '^[AEIOUaeiou]' AND CITY NOT REGEXP '[AEIOUaeiou]$';
```
