### Q:
- Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

### Solution
- Use regex
```sql
SELECT DISTINCT city FROM station WHERE city REGEXP "^[^aeiou].*";
```