### Table: Logs
```sql
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
```
- id is the primary key for this table.

### Write an SQL query to find all numbers that appear at least three times consecutively.

### Return the result table in any order.

### The query result format is in the following example:
- Logs table:  
```sql
+----+-----+
| Id | Num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
```
- Result table:  
```sql
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
```
- 1 is the only number that appears consecutively for at least three times.  

### Solution
- WHERE current num equal to last and last last one
```sql
SELECT DISTINCT num as ConsecutiveNums 
FROM
(
SELECT num, lag(num) over() as Lag1,
lead(num) over() as Lead1
FROM LOGS
) as A
WHERE A.num = A.Lag1 and A.num = A.Lead1;
```