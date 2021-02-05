### The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.


```sql
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
```

### Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.
```sql
+----------+
| Employee |
+----------+
| Joe      |
+----------+
```

### Solution
- WHERE current num equal to last and last last one
```sql
SELECT name as Employee FROM employee e WHERE salary > (SELECT salary FROM employee WHERE id = e.managerid);
```