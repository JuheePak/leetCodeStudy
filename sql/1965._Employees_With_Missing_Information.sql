SELECT employee_id
FROM(
SELECT Employees.employee_id
FROM Employees
UNION ALL
SELECT Salaries.employee_id
FROM Salaries
) AS TBL1
GROUP BY employee_id
HAVING COUNT(*)=1 -- 특이한 문법
ORDER BY employee_id ASC;
