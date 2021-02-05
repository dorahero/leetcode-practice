### Write a SQL query to get the nth highest salary from the Employee table.
```sql
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```

### For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.
```sql
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
```

### Solution
- SQL is start from 0, so 0 is first one record  
- offset like chose the Nth record
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N = N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT
      ifnull((select distinct(Salary) from Employee order by Salary desc limit 1 offset N),null)
  );
END
```