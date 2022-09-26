-- Write your MySQL query statement below
SELECT C.name AS Customers
FROM Customers as C
LEFT JOIN Orders as O
ON C.id = O.customerId
WHERE O.customerId is null;