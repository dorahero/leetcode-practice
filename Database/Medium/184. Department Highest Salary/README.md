### The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

```sql
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
```

### The Department table holds all departments of the company.
```sql
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
```

### Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, your SQL query should return the following rows (order of rows does not matter).
```sql
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
```
Explanation:  
Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.
### Solution
- join and subquery
```sql
SELECT d.name as Department, e.name as Employee, e.salary as Salary 
FROM employee e, department d 
WHERE e.departmentid = d.id AND salary IN 
(
    SELECT MAX(salary) FROM employee GROUP BY departmentid HAVING departmentid = e.departmentid
) ORDER BY Salary DESC;
```