### Write a SQL query to get the second highest salary from the Employee table.

```sql
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```

### For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.
```sql
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```
### Solution
- IFNULL - IFNULL(A, B) -> A is null, then return B.
```sql
SELECT IFNULL((SELECT distinct(Salary) from Employee order by Salary desc limit 1 offset 1), null) SecondHighestSalary;
```