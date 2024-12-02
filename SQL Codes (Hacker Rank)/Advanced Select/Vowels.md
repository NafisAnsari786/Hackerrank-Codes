<img src="https://img.shields.io/badge/EASY-green" alt="EASY" width="70">


### **Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.**

Input Format

The STATION table is described as follows:

![image](https://github.com/user-attachments/assets/28c60e0c-332b-4e45-909b-44bd8b045a05)


**SOLUTION** 

```SQL
SELECT DISTINCT(CITY) FROM STATION
WHERE CITY NOT REGEXP '^[AEIOUaeiou]' AND CITY NOT REGEXP '[AEIOUaeiou]$';
```
