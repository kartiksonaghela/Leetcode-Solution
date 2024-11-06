WITH RankedSalaries AS (
    SELECT 
        e.id,
        e.name AS employee_name,
        e.salary,
        e.departmentId,
        d.name AS department_name,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank
    FROM employee e
    JOIN department d ON e.departmentId = d.id
)
SELECT department_name AS Department, 
       employee_name AS Employee, 
       salary AS Salary
FROM RankedSalaries
WHERE salary_rank <= 3
ORDER BY department_name, salary DESC;
