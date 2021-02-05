### Q:
- Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.  

The column id is continuous increment.  

Mary wants to change seats for the adjacent students.  

Can you write a SQL query to output the result for Mary?  

```sql
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
```

### For the sample input, the output is:
```sql
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
```
Note : If the number of students is odd, there is no need to change the last one's seat.  
### Solution
- Self join
```sql
SELECT s1.id id, s2.student student FROM seat s1, seat s2 WHERE (s1.id%2 = 1 AND s1.id = s2.id-1)
OR (s1.id%2 = 0 AND s1.id-1 = s2.id)
OR (s1.id%2 = 1 AND s1.id = s2.id AND s1.id+1 > (SELECT MAX(id) FROM seat))
ORDER BY id;   
```