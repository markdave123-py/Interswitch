WITH EmployeeHierarchy AS (

    SELECT
        employee_id,
        First_Name + ' ' + Last_Name AS Employee_Name,
        manager_id,
        CAST(NULL AS NVARCHAR(MAX)) AS Manager_Name,
        0 AS Level
    FROM Employees

    UNION ALL

    SELECT
        e.employee_id,
        e.First_Name + ' ' + e.Last_Name AS Employee_Name,
        e.manager_id,
        eh.Employee_Name AS Manager_Name,
        Level + 1
    FROM Employees e
    INNER JOIN EmployeeHierarchy eh
        ON e.manager_id = eh.employee_id
)

SELECT
    Employee_Name AS Employee,
    Manager_Name AS Reports_To,
    Level AS Hierarchy_Level
FROM EmployeeHierarchy
ORDER BY Employee, Hierarchy_Level;
