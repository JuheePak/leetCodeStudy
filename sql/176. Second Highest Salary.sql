-- Write your MySQL query statement below
SELECT ifnull((SELECT distinct salary FROM Employee order by salary DESC limit 1,1), null) AS SecondHighestSalary;