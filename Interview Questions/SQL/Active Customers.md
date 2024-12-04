<img src="https://img.shields.io/badge/MEDIUM-orange" alt="MEDIUM" width="70">

![image](https://github.com/user-attachments/assets/73a364c7-aede-47f1-be5c-6022b80061de)

**SOLUTION**

```SQL
WITH ActiveCustomers AS (
    SELECT CUSTOMERID, 
           CASE   
               WHEN DATEDIFF(LASTPURCHASEDATE, JOINDATE) <= 180 
               THEN DATEDIFF(LASTPURCHASEDATE, JOINDATE) 
               ELSE 0 
           END AS ActiveDays
    FROM CustomerData
)
SELECT COUNT(*) AS ActiveCustomerCount 
FROM ActiveCustomers
WHERE ActiveDays > 0;
```

![Uploading image.png…]()
