<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

Generate the following two result sets:

Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). 
For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:
```text
"There are a total of [occupation_count] [occupation]s."
```
where [occupation_count] is the number of occurrences of an occupation in OCCUPATIONS and [occupation] is the lowercase occupation name. If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.

Note: There will be at least two entries in the table for each type of occupation.

Sample Input

![image](https://github.com/user-attachments/assets/2470312b-942a-45d5-a0d3-7fb1ca78908f)

Sample Output  

Ashely(P)
Christeen(P) 
Jane(A)
Jenny(D)
Julia(A)
Ketty(P)
Maria(A)
Meera(S)
Priya(S)
Samantha(D)
There are a total of 2 doctors.
There are a total of 2 singers.
There are a total of 3 actors.
There are a total of 3 professors.

**SOLUTION**

```sql
select concat(name,'(',left(occupation,1),')')
from occupations
order by name;

select concat('There are a total of ',count(occupation),' ',lower(occupation),'s.')
from occupations
group by occupation
order by count(occupation), occupation asc;
```
